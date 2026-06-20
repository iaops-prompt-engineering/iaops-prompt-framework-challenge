# Questao 08

## Framework

R-I-S-E

## Prompt

Role:

Voce e uma pessoa Staff SRE chamada para uma war room de producao. Doc Brown precisa de uma analise tecnica em ate 20 minutos para decidir entre rollback do deploy `v2.48.0` e scaling emergencial de RDS/pool de conexoes.

Input:

Deploy anterior:

```text
Deploy chronos-api: v2.47.0 -> v2.48.0
Argo CD sync: 2026-04-23 18:42:11 UTC
Changelog:
- Adicionado endpoint POST /v2/transactions/batch
- Refatorado cliente do Ledger (pool de conexoes movido para nova biblioteca interna)
- Bump de psycopg 3.1.18 -> 3.2.0
- Reduzido timeout do Ledger de 5s para 2s
```

Metricas Beacon:

```text
timestamp                p99_latency_ms   req_rate_s   err_rate_pct
2026-04-24 13:30 UTC     420              1200         0.2
2026-04-24 13:45 UTC     510              1450         0.3
2026-04-24 14:00 UTC     780              1780         0.8
2026-04-24 14:10 UTC     2400             2100         4.5
2026-04-24 14:15 UTC     5200             2400         8.2
2026-04-24 14:20 UTC     8100             2650         11.7
```

Logs:

```text
2026-04-24 14:19:48 [ERROR] [ledger-client] connection pool exhausted (max=20, active=20, waiting=147)
2026-04-24 14:19:49 [WARN]  [ledger-client] query timeout after 2000ms: SELECT ... FROM transactions WHERE ...
2026-04-24 14:19:49 [ERROR] [handler] POST /v2/transactions/batch failed: context deadline exceeded
2026-04-24 14:19:50 [ERROR] [ledger-client] connection reset by peer
2026-04-24 14:19:51 [WARN]  [circuit-breaker] ledger-client OPEN (threshold 50%, current 87%)
2026-04-24 14:19:52 [ERROR] [reactor] failed to publish message: chronos-api upstream error
```

Reactor:

- 50.127 mensagens acumuladas.
- Backlog crescendo a aproximadamente 800/min.
- Consumer lag atual de 18 minutos e aumentando.

Cluster:

- Chronos: 12/12 pods running.
- HPA no maximo.
- CPU medio dos pods: 62%.
- Memoria media dos pods: 71%.
- Conexoes ativas ao Ledger: 240/250.

Steps:

Produza um postmortem tecnico e decisorio com:

1. Resumo executivo.
2. Linha do tempo.
3. Impacto atual.
4. Hipotese de causa raiz mais provavel.
5. Evidencias que sustentam a hipotese.
6. Evidencias contra ou incertezas.
7. Decisao recomendada: rollback, scaling emergencial ou combinacao.
8. Acoes imediatas nos proximos 20 minutos.
9. Acoes de follow-up.
10. Riscos de cada alternativa.

Expectation:

A resposta deve ser direta, tecnica e orientada a decisao. Nao invente dados alem dos artefatos. Quando inferir algo, marque como inferencia. O ponto principal e recomendar claramente se Doc Brown deve fazer rollback do `v2.48.0`, scaling emergencial ou ambos.

