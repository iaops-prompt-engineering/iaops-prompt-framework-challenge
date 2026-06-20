# Questao 06

## Framework

C-A-R-E

## Prompt

Context:

A Hill Valley Tech tem um padrao interno de IaC para todo modulo Terraform:

- Tags obrigatorias em todo recurso: `Owner`, `CostCenter`, `Environment`.
- Prefixo `hvt-` nos nomes de recursos.
- Todo bucket S3 deve ter encryption habilitada com SSE-S3 no minimo.
- Versioning deve estar ativo.
- Block Public Access deve bloquear totalmente acesso publico.
- Logging deve estar configurado.
- Variaveis em `variables.tf` devem ter `description` e `type`.

Action:

Crie um modulo Terraform reutilizavel para buckets S3 aderente ao padrao interno. Inclua `main.tf`, `variables.tf`, `outputs.tf` e `examples/basic/main.tf`.

Result:

O resultado deve ser codigo Terraform limpo, reutilizavel, com nomes padronizados, tags comuns, bucket de logs configuravel e exemplo de consumo do modulo.

Example:

Use o estilo deste modulo VPC como referencia:

```hcl
variable "environment" {
  description = "Nome do ambiente (dev, staging, production)"
  type        = string
}

locals {
  common_tags = {
    Owner       = var.owner
    CostCenter  = var.cost_center
    Environment = var.environment
  }
}

resource "aws_vpc" "this" {
  cidr_block = var.cidr_block
  tags = merge(local.common_tags, {
    Name = "hvt-vpc-${var.environment}"
  })
}
```

Responda com os arquivos separados por cabecalhos no formato `## main.tf`, `## variables.tf`, `## outputs.tf` e `## examples/basic/main.tf`.

