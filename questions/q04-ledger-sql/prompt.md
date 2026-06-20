# Questao 04

## Framework

T-A-G

## Prompt

Crie uma query SQL PostgreSQL para gerar o relatorio mensal de transacoes completed do Ledger nos ultimos 6 meses corridos a partir de 2026-04-24.

Execute as seguintes acoes:

1. Use somente a tabela `transactions`, pois as metricas pedidas nao exigem colunas de `customers`.
2. Filtre apenas `status = 'completed'`.
3. Considere o periodo de 2025-10-24 00:00:00 ate antes de 2026-04-25 00:00:00, preservando o recorte de 6 meses corridos a partir da data informada.
4. Agrupe por mes no formato `YYYY-MM` e por `category`.
5. Retorne a quantidade de transacoes e o volume total em reais com 2 casas decimais, convertendo `amount_cents`.
6. Ordene por mes crescente e categoria crescente.

O objetivo e entregar uma SQL pronta para Jennifer usar no relatorio executivo de crescimento de transacoes por categoria.

Schema:

```sql
CREATE TABLE transactions (
  id              BIGSERIAL PRIMARY KEY,
  customer_id     BIGINT NOT NULL REFERENCES customers(id),
  category        VARCHAR(32) NOT NULL,
  amount_cents    BIGINT NOT NULL,
  status          VARCHAR(16) NOT NULL,
  payment_method  VARCHAR(16),
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at    TIMESTAMPTZ
);

CREATE INDEX idx_transactions_created_at ON transactions(created_at);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_category ON transactions(category);
```

Responda somente com a query SQL.

