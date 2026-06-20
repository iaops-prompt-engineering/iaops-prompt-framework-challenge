# Questao 01

## Framework

R-T-F

## Prompt

Voce e um engenheiro DevOps especialista em containers, Python e Kubernetes.

Crie um Dockerfile de producao para a aplicacao Lift, uma API Python/Flask que escuta na porta 8080. O projeto tem esta estrutura:

```text
lift/
├── app.py
├── requirements.txt
├── lib/
│   ├── auth.py
│   └── storage.py
└── tests/
    └── test_app.py
```

O arquivo `requirements.txt` contem:

```text
Flask==3.0.0
gunicorn==21.2.0
requests==2.31.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
```

Em producao, o servico deve subir com:

```bash
gunicorn --bind 0.0.0.0:8080 --workers 4 app:app
```

O runtime precisa receber as variaveis de ambiente `DATABASE_URL` e `API_KEY`. Siga boas praticas: imagem base enxuta, usuario nao-root, cache eficiente de dependencias, variaveis Python adequadas, exposicao da porta correta, sem copiar arquivos desnecessarios e sem embutir segredos.

Responda somente com o conteudo completo do `Dockerfile`, sem explicacoes.

