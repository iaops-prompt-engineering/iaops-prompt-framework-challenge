# Modelo

Claude Sonnet 4 - escolhido pela boa qualidade na organizacao de procedimentos, criterios de escalacao e comunicacao operacional.

## Output

# Runbook: High Memory Usage on Chronos API Pods

## 1. Confirmar alerta

```bash
kubectl top pods -n production -l app.kubernetes.io/name=chronos-api
kubectl get hpa -n production
```

Verificacao esperada: um ou mais pods acima de 85% do limite de memoria por pelo menos 10 minutos. O HPA deve estar visivel com min 4 e max 12.

## 2. Identificar pods afetados

```bash
kubectl get pods -n production -l app.kubernetes.io/name=chronos-api -o wide
kubectl describe pods -n production -l app.kubernetes.io/name=chronos-api
```

Verificacao esperada: pods em `Running`, sem `OOMKilled` recente. Se houver `OOMKilled`, registrar os nomes dos pods e horarios.

## 3. Verificar consumo de memoria e restarts

```bash
kubectl top pods -n production -l app.kubernetes.io/name=chronos-api --containers
kubectl get pods -n production -l app.kubernetes.io/name=chronos-api \
  -o custom-columns=NAME:.metadata.name,RESTARTS:.status.containerStatuses[0].restartCount,PHASE:.status.phase
```

Verificacao esperada: identificar se o consumo e distribuido em todos os pods ou concentrado em poucos pods.

## 4. Verificar HPA e capacidade atual

```bash
kubectl describe hpa -n production chronos-api
kubectl get deployment -n production chronos-api
```

Verificacao esperada: confirmar replicas atuais, limites do HPA e se o HPA ja chegou ao maximo de 12 replicas.

## 5. Consultar eventos Kubernetes

```bash
kubectl get events -n production --sort-by=.lastTimestamp | tail -n 50
```

Verificacao esperada: procurar `OOMKilled`, falhas de scheduling, problemas de probe ou throttling.

## 6. Consultar logs do Chronos

```bash
kubectl logs -n production deploy/chronos-api --since=30m --all-containers=true | grep -Ei "error|warn|memory|oom|ledger|reactor"
```

Verificacao esperada: identificar aumento de erros, timeouts com Ledger, falhas no Reactor ou indicios de memory leak.

## 7. Validar dependencias

Ledger:

```bash
kubectl logs -n production deploy/chronos-api --since=30m | grep -Ei "ledger|postgres|connection|timeout"
```

Reactor:

```bash
aws sqs get-queue-attributes \
  --queue-url "<chronos-transactions-queue-url>" \
  --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible
```

Verificacao esperada: confirmar se a memoria alta acompanha timeouts do Ledger, backlog no Reactor ou retries em massa.

## 8. Checar status do deploy no Argo CD

```bash
argocd app get chronos-api
argocd app history chronos-api
```

Verificacao esperada: confirmar se houve deploy recente correlacionado com o inicio do alerta.

## 9. Mitigacoes seguras

Se apenas um pod estiver degradado:

```bash
kubectl delete pod -n production <pod-name>
```

Se todos os pods estiverem acima de 85% e o HPA nao estiver no maximo:

```bash
kubectl scale deployment chronos-api -n production --replicas=8
```

Se o HPA ja estiver no maximo ou houver OOMKilled recorrente, nao aumentar recursos manualmente sem alinhamento com `@chronos-core`.

Verificacao esperada: memoria abaixo de 80%, erro estabilizado e pods novos prontos.

## 10. Escalar para o time senior

Escalar para `@chronos-core` em `#oncall-chronos` se qualquer criterio ocorrer:

- Memoria permanece acima de 85% por mais de 20 minutos apos mitigacao.
- HPA esta em 12 replicas e o alerta continua.
- Ha `OOMKilled` recorrente.
- Erro HTTP 5xx ou latencia p99 aumenta junto com o alerta.
- Logs indicam memory leak, falha no Ledger ou backlog crescente no Reactor.
- Deploy recente aparece como possivel causa.

Mensagem sugerida:

```text
@chronos-core incidente em Chronos: High memory usage >85% por <duracao>.
Estado: replicas=<n>, HPA=<estado>, pods afetados=<lista>, restarts=<n>.
Evidencias: <logs/metricas>.
Mitigacao aplicada: <acao>.
Impacto observado: <latencia/erro/backlog>.
```

## 11. Encerrar incidente

Encerrar somente quando:

- Memoria dos pods ficar abaixo de 80% por 15 minutos.
- Nao houver novos `OOMKilled`.
- Latencia e erro voltarem ao baseline.
- HPA estiver estavel.
- Ledger e Reactor nao apresentarem sintomas correlacionados.

Registrar no canal:

```text
Incidente encerrado: memoria do Chronos estabilizada abaixo de 80% por 15 min.
Causa provavel: <resumo>.
Acao aplicada: <acao>.
Follow-up: <ticket/link>.
```
