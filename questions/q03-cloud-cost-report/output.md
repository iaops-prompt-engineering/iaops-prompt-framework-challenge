# Modelo

Claude Sonnet 4 - escolhido pela boa organizacao de analise tabular, calculos percentuais e relatorio executivo.

## Output

# Relatorio de Reducao de Custos Cloud

## Resumo executivo

O custo mensal atual e de **USD 41.800**. A meta de 15% representa **USD 6.270/mes**. A combinacao recomendada abaixo estima economia de **USD 6.455/mes**, equivalente a **15,44%** da conta, sem acao que reduza SLA diretamente.

## Oportunidades priorizadas

| Prioridade | Oportunidade | Servicos afetados | Economia estimada | % da conta | Esforco | Riscos / pre-requisitos |
|---|---|---|---:|---:|---|---|
| 1 | Rightsizing de EC2 on-demand com uso medio de 45% | EC2 on-demand | USD 2.460 | 5,89% | Medio | Validar sazonalidade, workloads variaveis e limites de autoscaling |
| 2 | Otimizacao de EKS: ajustar requests, node groups e consolidacao de clusters | EKS | USD 1.340 | 3,21% | Alto | Exige analise de capacidade, testes de carga e janelas controladas |
| 3 | Reduzir retencao e filtrar logs de baixo valor | CloudWatch Logs | USD 1.120 | 2,68% | Baixo | Validar requisitos de auditoria e investigacao |
| 4 | Rightsizing de RDS com Performance Insights e ajuste de storage/instancia | RDS PostgreSQL | USD 820 | 1,96% | Medio | Confirmar picos, replicas, conexoes e impacto em multi-AZ |
| 5 | Lifecycle policies para S3 Standard | S3 Standard | USD 775 | 1,85% | Baixo | Classificar dados acessados raramente e validar restauracao |
| 6 | Revisao de NAT Gateway e trafego entre AZ/VPC | NAT Gateway | USD 300 | 0,72% | Medio | Mapear rotas e evitar quebra de egress de workloads privados |
| 7 | Reducao de Data Transfer Out entre regioes | Data Transfer Out | USD 285 | 0,68% | Medio | Depende de arquitetura e localidade dos consumidores |
| 8 | Otimizacao de ElastiCache com uso medio de 40% | ElastiCache Redis | USD 420 | 1,00% | Medio | Validar memoria, evictions, failover e throughput |

## Quick wins

| Acao | Economia estimada | % da conta |
|---|---:|---:|
| Reduzir retencao de CloudWatch Logs e aplicar filtros | USD 1.120 | 2,68% |
| Aplicar lifecycle policies em S3 | USD 775 | 1,85% |
| Revisar NAT Gateway ocioso ou duplicado | USD 300 | 0,72% |

Total quick wins: **USD 2.195/mes**, ou **5,25%** da conta.

## Iniciativas estruturais

| Acao | Economia estimada | % da conta |
|---|---:|---:|
| Rightsizing EC2 on-demand | USD 2.460 | 5,89% |
| Otimizacao EKS | USD 1.340 | 3,21% |
| Rightsizing RDS | USD 820 | 1,96% |

Total estrutural recomendado: **USD 4.620/mes**, ou **11,05%** da conta.

## Plano recomendado

Executar primeiro as acoes de baixo risco em CloudWatch Logs e S3, em seguida iniciar rightsizing de EC2 on-demand e RDS com base em metricas de pico. Em paralelo, abrir uma frente de otimizacao EKS com testes de carga e rollout gradual.

Combinacao recomendada para a meta:

- CloudWatch Logs: USD 1.120
- S3 Standard: USD 775
- EC2 on-demand: USD 2.460
- EKS: USD 1.340
- RDS PostgreSQL: USD 820

Economia total: **USD 6.515/mes**, **15,59%** da conta.

## Riscos principais

- Reducao agressiva de capacidade pode afetar SLA em picos.
- Logs com retencao menor podem reduzir capacidade de auditoria e troubleshooting.
- Alteracoes em EKS e RDS exigem metricas de pico, testes e plano de rollback.
