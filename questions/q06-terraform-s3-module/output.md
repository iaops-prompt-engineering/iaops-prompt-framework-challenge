# Modelo

GPT-4o - escolhido pela boa consistencia em Terraform AWS, modularizacao e padroes de compliance.

## Output

## main.tf

```hcl
locals {
  bucket_name = "hvt-${var.name}-${var.environment}"

  common_tags = {
    Owner       = var.owner
    CostCenter  = var.cost_center
    Environment = var.environment
  }
}

resource "aws_s3_bucket" "this" {
  bucket = local.bucket_name

  tags = merge(local.common_tags, {
    Name = local.bucket_name
  })
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.this.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_logging" "this" {
  bucket = aws_s3_bucket.this.id

  target_bucket = var.logging_bucket
  target_prefix = "s3/${local.bucket_name}/"
}
```

## variables.tf

```hcl
variable "name" {
  description = "Nome logico do bucket, sem o prefixo hvt e sem o ambiente"
  type        = string
}

variable "environment" {
  description = "Nome do ambiente (dev, staging, production)"
  type        = string
}

variable "owner" {
  description = "Responsavel pelo recurso"
  type        = string
}

variable "cost_center" {
  description = "Centro de custo associado ao recurso"
  type        = string
}

variable "logging_bucket" {
  description = "Nome do bucket S3 que recebera logs de acesso"
  type        = string
}
```

## outputs.tf

```hcl
output "bucket_name" {
  description = "Nome do bucket criado"
  value       = aws_s3_bucket.this.bucket
}

output "bucket_arn" {
  description = "ARN do bucket criado"
  value       = aws_s3_bucket.this.arn
}

output "bucket_id" {
  description = "ID do bucket criado"
  value       = aws_s3_bucket.this.id
}
```

## examples/basic/main.tf

```hcl
module "ledger_exports_bucket" {
  source = "../.."

  name           = "ledger-exports"
  environment    = "production"
  owner          = "data-platform"
  cost_center    = "finops-001"
  logging_bucket = "hvt-s3-access-logs-production"
}
```
