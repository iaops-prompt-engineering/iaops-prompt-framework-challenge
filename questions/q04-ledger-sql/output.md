# Modelo

GPT-4o - escolhido pela boa precisao em SQL PostgreSQL e conversao de requisitos de negocio em agregacoes.

## Output

```sql
SELECT
  to_char(date_trunc('month', created_at), 'YYYY-MM') AS month,
  category,
  count(*) AS transaction_count,
  round((sum(amount_cents)::numeric / 100), 2) AS total_amount_brl
FROM transactions
WHERE status = 'completed'
  AND created_at >= TIMESTAMPTZ '2025-10-24 00:00:00'
  AND created_at <  TIMESTAMPTZ '2026-04-25 00:00:00'
  AND category IN ('subscription', 'one_time', 'refund', 'credit_adjustment')
GROUP BY
  date_trunc('month', created_at),
  category
ORDER BY
  date_trunc('month', created_at) ASC,
  category ASC;
```
