# Questao 02

## Framework

R-T-F

## Prompt

Voce e uma engenheira SRE especialista em PostgreSQL, Linux, AWS S3 e automacao de backups.

Crie um script Bash robusto para backup diario do banco Ledger com estes parametros:

- Host: `ledger-db.internal.hvt.io`
- Porta: `5432`
- Banco: `ledger_prod`
- Usuario: `backup_user`
- Senha: variavel de ambiente `PGPASSWORD`, populada pelo AWS Secrets Manager via IAM role da instancia
- Regiao AWS: `us-east-1`
- Sistema operacional: Ubuntu 22.04 LTS
- Diretorio de trabalho: `/var/backups/ledger`
- Espaco livre disponivel: 80 GB
- Tamanho medio do dump compactado: aproximadamente 12 GB
- Bucket S3: `hvt-ledger-backups`
- Log: `/var/log/ledger-backup.log`

O script deve executar `pg_dump`, compactar com `gzip`, enviar o arquivo com `aws s3 cp`, manter 30 dias de retencao no S3 removendo backups mais antigos, registrar cada etapa com timestamp e sair com exit code diferente de zero em caso de falha. Inclua validacoes de dependencias, checagem de `PGPASSWORD`, criacao do diretorio se necessario e limpeza segura de arquivos temporarios locais.

Responda somente com o script Bash completo, incluindo shebang e opcoes de shell adequadas.

