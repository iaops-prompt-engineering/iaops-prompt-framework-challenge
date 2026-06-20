# Justificativa

## Framework escolhido: R-I-S-E

Escolhi R-I-S-E porque o cenario e uma investigacao tecnica com muitos artefatos e uma decisao urgente. O Role define uma Staff SRE em war room; o Input concentra deploy, metricas, logs, Reactor e cluster; o Steps forca linha do tempo, impacto, evidencias, incertezas e decisao; o Expectation exige recomendacao clara sem inventar dados.

## Comparacao com R-T-F

R-T-F tambem funcionaria para definir Staff SRE, tarefa e formato do postmortem. O ganho seria simplicidade; a perda seria menor controle sobre os artefatos e sobre a sequencia de raciocinio, que sao centrais neste incidente.

## Comparacao com T-A-G

T-A-G tambem seria razoavel para "analisar incidente", "correlacionar deploy, metricas e logs" e "decidir rollback ou scaling". O ganho seria foco no objetivo decisorio; a perda seria que T-A-G organiza pior os muitos inputs e as verificacoes esperadas.

## O que nao funcionou tao bem

B-A-B foi descartado porque o problema nao e transformar um estado antigo em novo, e sim diagnosticar e decidir durante um incidente. Ele ajudaria a comparar antes/depois do deploy, mas perderia rigor para evidencias, incertezas e plano imediato.
