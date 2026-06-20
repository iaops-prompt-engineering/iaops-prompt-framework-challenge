# Questao 05

## Framework

B-A-B

## Prompt

Before:

O manifest atual do Chronos API e legado, roda com apenas 1 replica, usa imagem `chronos-api:latest`, contem secrets hardcoded e nao define probes, recursos ou securityContext.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: chronos-api
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: chronos-api
  template:
    metadata:
      labels:
        app: chronos-api
    spec:
      containers:
      - name: api
        image: chronos-api:latest
        ports:
        - containerPort: 8080
        env:
        - name: DB_PASSWORD
          value: "P@ssw0rd2023!"
        - name: JWT_SECRET
          value: "hvt-jwt-prod-secret"
```

After:

Quero uma versao moderna para producao com alta disponibilidade, imagem versionada, secrets fora do manifest, resource requests e limits, liveness e readiness probes, securityContext nao-root, rollout seguro e boas praticas Kubernetes para uma API HTTP na porta 8080.

Bridge:

Transforme o manifest legado em um YAML Kubernetes completo e pronto para aplicar. Use `chronos-api:v2.48.0` como imagem, 3 replicas, referencias a um Secret chamado `chronos-api-secrets` para `DB_PASSWORD` e `JWT_SECRET`, probes em `/healthz` e `/readyz`, labels consistentes e estrategia rolling update. Responda somente com o YAML final.

