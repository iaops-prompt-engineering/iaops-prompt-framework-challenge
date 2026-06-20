# Lessons Learned

## O que funcionou

- R-T-F funcionou bem para entregas tecnicas fechadas, como Dockerfile e script bash.
- T-A-G foi adequado para transformar dados e requisitos de negocio em relatorios e SQL.
- B-A-B facilitou a modernizacao do manifest Kubernetes porque o contraste entre legado e estado alvo era explicito.
- C-A-R-E ajudou a preservar padrao interno de IaC por incluir exemplo de estilo.
- R-I-S-E foi o melhor framework para runbooks e incidentes por separar entradas, passos e expectativa.

## O que nao funcionou tao bem

- Prompts sem formato final tendem a retornar explicacoes junto com codigo.
- Para outputs operacionais, pedir criterios objetivos evita respostas genericas.
- Em incidentes, frameworks simples demais deixam de capturar evidencias e trade-offs.

## Qual modelo respondeu melhor

O melhor desempenho geral foi do OpenAI GPT-4o nas questoes com codigo e infraestrutura. Anthropic Claude Sonnet 4 teve boa qualidade textual para runbooks, Kubernetes, postmortem e relatorios estruturados.

## Prompts que precisaram de refinamento

- Q03 precisou explicitar que cada oportunidade deveria incluir percentual da conta total.
- Q05 precisou reforcar que secrets nao poderiam permanecer inline no manifest.
- Q08 precisou pedir recomendacao decisoria, nao apenas resumo do incidente.
