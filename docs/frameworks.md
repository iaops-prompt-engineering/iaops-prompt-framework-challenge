# Frameworks

## R-T-F

Role, Task, Format.

- Quando usar: tarefas objetivas em que a identidade tecnica do modelo e o formato final importam.
- Vantagens: simples, direto e reduz ambiguidade de saida.
- Limitacoes: menos rico para raciocinio comparativo ou mudanca de estado.
- Exemplo rapido: "Voce e um engenheiro DevOps. Crie um Dockerfile. Responda apenas com o arquivo final."

## T-A-G

Task, Action, Goal.

- Quando usar: analises orientadas a objetivo, relatorios e consultas.
- Vantagens: conecta acao tecnica com resultado esperado.
- Limitacoes: nao explicita persona nem formato com a mesma forca do R-T-F.
- Exemplo rapido: "Analise custos, priorize oportunidades e alcance 15% de reducao sem degradar SLA."

## B-A-B

Before, After, Bridge.

- Quando usar: modernizacao, refatoracao e transformacao de estado atual para estado desejado.
- Vantagens: evidencia lacunas entre legado e padrao alvo.
- Limitacoes: menos adequado para tarefas sem um antes/depois claro.
- Exemplo rapido: "Antes: manifest inseguro. Depois: deployment produtivo seguro. Ponte: gere o YAML modernizado."

## C-A-R-E

Context, Action, Result, Example.

- Quando usar: entregas que precisam seguir padrao interno ou exemplo existente.
- Vantagens: combina contexto, acao, resultado e referencia de estilo.
- Limitacoes: pode ficar extenso quando o problema e simples.
- Exemplo rapido: "Contexto: padrao IaC. Acao: criar modulo S3. Resultado: arquivos Terraform. Exemplo: estilo do modulo VPC."

## R-I-S-E

Role, Input, Steps, Expectation.

- Quando usar: procedimentos, runbooks, investigacoes e analises com multiplos artefatos.
- Vantagens: organiza entradas e passos esperados, reduzindo saltos logicos.
- Limitacoes: mais verboso que frameworks diretos como R-T-F.
- Exemplo rapido: "Voce e SRE. Use os artefatos abaixo. Siga diagnostico, mitigacao e escalacao. Entregue runbook executavel."

