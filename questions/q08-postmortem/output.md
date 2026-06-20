# Modelo

Claude Sonnet 4 - escolhido pela boa capacidade de correlacionar metricas, logs, deploy e trade-offs operacionais sob pressao.

## Output

# Postmortem tecnico: incidente Chronos / Ledger

## Resumo executivo

Recomendacao: executar **rollback imediato do Chronos API de `v2.48.0` para `v2.47.0`** e preparar scaling emergencial do Ledger apenas como contingencia se a recuperacao nao ocorrer em 10 a 15 minutos.

A causa mais provavel e regressao introduzida no `v2.48.0`, relacionada ao novo cliente do Ledger, novo endpoint batch, alteracao do pool de conexoes e reducao do timeout de 5s para 2s. O gargalo atual nao parece ser CPU ou memoria do Chronos: o HPA ja esta no maximo, CPU media esta em 62% e memoria em 71%. O sintoma dominante e exaustao de conexoes com o Ledger.

## Linha do tempo

| Horario UTC | Evento |
|---|---|
| 2026-04-23 18:42 | Deploy `chronos-api v2.47.0 -> v2.48.0` via Argo CD |
| 2026-04-24 13:30 | p99 420 ms, erro 0,2%, req/s 1200 |
| 2026-04-24 14:00 | p99 780 ms, erro 0,8%, req/s 1780 |
| 2026-04-24 14:10 | p99 2400 ms, erro 4,5%, req/s 2100 |
| 2026-04-24 14:15 | p99 5200 ms, erro 8,2%, req/s 2400 |
| 2026-04-24 14:20 | p99 8100 ms, erro 11,7%, req/s 2650 |
| 2026-04-24 14:19 | Logs mostram pool do Ledger esgotado, timeouts, circuit breaker aberto e falha no Reactor |

## Impacto atual

- Latencia p99 aumentou de 420 ms para 8100 ms.
- Taxa de erro subiu de 0,2% para 11,7%.
- Reactor acumula 50.127 mensagens, crescendo 800/min.
- Consumer lag esta em 18 minutos e aumentando.
- Ledger esta com 240/250 conexoes ativas.
- Chronos esta em 12/12 pods, com HPA no maximo.

## Causa raiz mais provavel

Inferencia: a versao `v2.48.0` aumentou pressao sobre o Ledger e tornou o sistema menos tolerante a latencia ao mover o pool de conexoes para uma biblioteca nova, adicionar o endpoint batch e reduzir timeout do Ledger para 2s.

O pool local reporta `max=20, active=20, waiting=147`. Com 12 pods, isso pode explicar ate 240 conexoes ativas, exatamente proximo do limite observado do RDS, 240/250.

## Evidencias a favor

- O changelog inclui mudancas diretamente relacionadas ao Ledger.
- Logs mostram `connection pool exhausted`, `query timeout after 2000ms` e `connection reset by peer`.
- O endpoint novo `POST /v2/transactions/batch` aparece falhando.
- HPA no maximo nao resolveu, sugerindo que adicionar pods pode ampliar consumo de conexoes.
- CPU e memoria nao estao saturadas, reduzindo probabilidade de gargalo no compute do Chronos.
- Conexoes ao Ledger estao quase no limite.

## Incertezas

- Nao ha metrica historica de conexoes do Ledger antes do deploy.
- Nao ha confirmacao de que todo o aumento de trafego veio do novo endpoint batch.
- Nao ha plano de execucao das queries no trecho de log.
- Pode existir componente de pico real de trafego, pois req/s subiu de 1200 para 2650.

## Decisao recomendada

Executar rollback primeiro.

Motivos:

- O deploy alterou exatamente os componentes que aparecem nos erros.
- Scaling de Chronos nao ajuda porque o HPA ja chegou ao maximo.
- Aumentar pods pode piorar a pressao de conexoes no Ledger.
- Scaling emergencial do RDS e pool pode mascarar regressao e aumentar risco de saturacao do banco.

Preparar scaling emergencial como fallback se, apos rollback, conexoes, erro e p99 nao melhorarem em 10 a 15 minutos.

## Acoes imediatas

1. Pausar novas mudancas no Chronos.
2. Executar rollback para `v2.47.0` via Argo CD.
3. Monitorar por 15 minutos:
   - p99 latency.
   - error rate.
   - conexoes Ledger.
   - backlog Reactor.
   - circuit breaker do Ledger.
4. Se rollback estabilizar erro e latencia, manter `v2.47.0`.
5. Se rollback nao estabilizar, aumentar temporariamente limite de conexoes/pool com aprovacao de banco e SRE senior.

## Follow-up

- Revisar implementacao do novo pool de conexoes.
- Reavaliar timeout de 2s para Ledger.
- Adicionar limite de concorrencia no endpoint batch.
- Criar teste de carga para `/v2/transactions/batch`.
- Adicionar metricas por endpoint, pool, waiters e circuit breaker.
- Definir budget de conexoes por pod para nao exceder limite do RDS.

## Riscos das alternativas

| Alternativa | Ganho | Risco |
|---|---|---|
| Rollback | Remove rapidamente a regressao mais provavel | Se o pico for causa principal, pode nao resolver sozinho |
| Scaling RDS/pool | Aumenta capacidade de conexoes | Pode mascarar bug, elevar custo e aumentar carga no banco |
| Ambos simultaneamente | Maior chance de aliviar rapido | Dificulta identificar causa e aumenta risco operacional |
