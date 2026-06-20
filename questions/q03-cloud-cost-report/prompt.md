# Questao 03

## Framework

T-A-G

## Prompt

Analise o CSV de custos AWS abaixo e produza um relatorio executivo de oportunidades para reduzir 15% do custo cloud no proximo trimestre sem degradar SLA.

Execute as seguintes acoes:

1. Calcule o custo total mensal.
2. Identifique oportunidades de economia priorizadas por impacto.
3. Para cada oportunidade, estime economia mensal em USD, percentual sobre a conta total, esforco de implementacao (baixo, medio ou alto) e riscos ou pre-requisitos.
4. Separe quick wins de iniciativas estruturais.
5. Indique uma combinacao recomendada para atingir pelo menos 15% de reducao.

O objetivo e entregar para Goldie Wilson uma recomendacao clara, priorizada e acionavel, conectando economia, risco e preservacao de SLA.

CSV:

```csv
servico,categoria,custo_mensal_usd,uso_medio_pct,observacao
EC2 reservada,compute,4200,72,contrato de 1 ano
EC2 on-demand,compute,8200,45,workloads variaveis
EKS,compute,6700,58,3 clusters
RDS PostgreSQL,databases,8200,62,multi-AZ
ElastiCache Redis,databases,2100,40,cluster de producao
S3 Standard,storage,3100,,5 buckets principais
EBS gp3,storage,1600,68,volumes de producao
CloudWatch Logs,observability,2800,,retencao de 90 dias
CloudWatch Metrics,observability,900,,
Data Transfer Out,network,1900,,trafego entre regioes
NAT Gateway,network,1200,,3 gateways ativos
Lambda,compute,900,30,~12M invocacoes/mes
```

Formato esperado: resumo executivo, tabela de oportunidades, plano recomendado e riscos principais.

