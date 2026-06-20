# Justificativa

O Before descreve o manifest legado: 1 replica, imagem `latest`, secrets hardcoded e ausencia de probes, resources e securityContext.
O After define o estado moderno esperado: alta disponibilidade, imagem versionada, secrets externos, probes, resources e execucao nao-root.
O Bridge aparece na instrucao para transformar o YAML legado em um manifest completo com `chronos-api:v2.48.0`, 3 replicas e rolling update.
