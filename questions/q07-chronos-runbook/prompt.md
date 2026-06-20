# Questao 07

## Framework

R-I-S-E

## Prompt

Role:

Voce e uma lider SRE escrevendo um runbook para plantonistas que podem nao conhecer internamente o Chronos.

Input:

Alerta recorrente do Beacon: `[CRITICAL] High memory usage on Chronos API pods (>85% for 10min)`.

Contexto operacional:

- Chronos roda no EKS.
- Namespace: `production`.
- 6 replicas com HPA configurado: min 4, max 12, CPU target 70%.
- Deploy via Argo CD a partir do repositorio `hvt/chronos-api`.
- Dependencias diretas: Ledger PostgreSQL e Reactor SQS.
- Observabilidade: endpoint `/metrics`, logs centralizados no Beacon e dashboards em Grafana.
- Ferramentas disponiveis: `kubectl`, `aws cli`, `argocd cli`.
- Canal de plantao: `#oncall-chronos`.
- Escalacao senior: `@chronos-core`, SLA de resposta de 15 minutos em horario comercial e 30 minutos fora.

Steps:

Crie um runbook procedural cobrindo:

1. Confirmacao do alerta.
2. Diagnostico inicial com comandos especificos.
3. Verificacao de pods, HPA, consumo de memoria, restarts e eventos Kubernetes.
4. Consulta de logs e metricas.
5. Validacao de dependencias Ledger e Reactor.
6. Mitigacoes seguras de curto prazo.
7. Criterios objetivos de escalacao.
8. Criterios de encerramento.
9. Comunicacao no Slack.

Expectation:

O runbook deve ser completo, direto, executavel por qualquer plantonista e conter a verificacao esperada ao final de cada passo. Use comandos reais e placeholders apenas quando inevitavel.

