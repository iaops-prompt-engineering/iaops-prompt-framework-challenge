# Modelo

GPT-4o - escolhido pela boa capacidade de gerar Bash defensivo com tratamento de erro, logs e comandos AWS/PostgreSQL coerentes.

## Output

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

DB_HOST="ledger-db.internal.hvt.io"
DB_PORT="5432"
DB_NAME="ledger_prod"
DB_USER="backup_user"
AWS_REGION="us-east-1"
BACKUP_DIR="/var/backups/ledger"
S3_BUCKET="hvt-ledger-backups"
LOG_FILE="/var/log/ledger-backup.log"
RETENTION_DAYS=30

timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

log() {
  echo "$(timestamp) $*" | tee -a "$LOG_FILE"
}

fail() {
  log "ERROR: $*"
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "Comando obrigatorio nao encontrado: $1"
}

cleanup() {
  if [[ -n "${TMP_FILE:-}" && -f "$TMP_FILE" ]]; then
    rm -f "$TMP_FILE"
  fi
}

trap cleanup EXIT

require_command pg_dump
require_command gzip
require_command aws
require_command find

[[ -n "${PGPASSWORD:-}" ]] || fail "Variavel PGPASSWORD nao definida"

mkdir -p "$BACKUP_DIR"
touch "$LOG_FILE" || fail "Nao foi possivel escrever no log $LOG_FILE"

BACKUP_DATE="$(date -u +"%Y%m%dT%H%M%SZ")"
BACKUP_FILE="ledger_prod_${BACKUP_DATE}.sql.gz"
TMP_FILE="${BACKUP_DIR}/${BACKUP_FILE}.tmp"
FINAL_FILE="${BACKUP_DIR}/${BACKUP_FILE}"
S3_URI="s3://${S3_BUCKET}/${BACKUP_FILE}"

log "Inicio do backup do banco ${DB_NAME}"

AVAILABLE_KB="$(df -Pk "$BACKUP_DIR" | awk 'NR==2 {print $4}')"
REQUIRED_KB=$((20 * 1024 * 1024))
if (( AVAILABLE_KB < REQUIRED_KB )); then
  fail "Espaco livre insuficiente em ${BACKUP_DIR}: ${AVAILABLE_KB} KB disponiveis"
fi

log "Executando pg_dump e compactacao gzip"
PGPASSWORD="$PGPASSWORD" pg_dump \
  --host "$DB_HOST" \
  --port "$DB_PORT" \
  --username "$DB_USER" \
  --dbname "$DB_NAME" \
  --format plain \
  --no-owner \
  --no-privileges \
  | gzip -9 > "$TMP_FILE"

mv "$TMP_FILE" "$FINAL_FILE"
log "Arquivo local criado: ${FINAL_FILE}"

log "Enviando backup para ${S3_URI}"
aws s3 cp "$FINAL_FILE" "$S3_URI" --region "$AWS_REGION" --only-show-errors

log "Aplicando retencao local de ${RETENTION_DAYS} dias"
find "$BACKUP_DIR" -type f -name "ledger_prod_*.sql.gz" -mtime +"$RETENTION_DAYS" -delete

log "Aplicando retencao no S3 de ${RETENTION_DAYS} dias"
CUTOFF="$(date -u -d "${RETENTION_DAYS} days ago" +"%Y-%m-%dT%H:%M:%SZ")"
aws s3api list-objects-v2 \
  --bucket "$S3_BUCKET" \
  --region "$AWS_REGION" \
  --query "Contents[?LastModified<='${CUTOFF}'].[Key]" \
  --output text |
while read -r key; do
  [[ -n "$key" && "$key" != "None" ]] || continue
  log "Removendo backup antigo do S3: ${key}"
  aws s3 rm "s3://${S3_BUCKET}/${key}" --region "$AWS_REGION" --only-show-errors
done

log "Backup concluido com sucesso: ${S3_URI}"
exit 0
```
