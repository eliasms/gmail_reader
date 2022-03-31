# Ler e-mails da caixa de entrada utilizando API do Gmail
Obter e-mails diretamente da API do Gmail com Python, o objetivo é no futuro criar um helper para ler conteúdos de e-mail em testes automatizados e2e, principalmente códigos de autenticação de dois fatores.

## Requisitos do ambiente de desenvolvimento:

### Criar o ambiente virtual com o venv:
```python -m venv venv```


### Instalar as dependências do projeto 
```pip install requirements.txt``` 


### Habilitar a execução do terminal virtual no PowerShell (caso queria utilizar o PS no Windows):

Abrir o PowerShell como administrador;

Digitar o comando: ```Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned```

Digitar "S" para alterar a politica de execução e teclar Enter.

### Iniciar o ambiente virtual no venv:
.\venv\Scripts\Activate.ps1

## Requisitos para fazer chamadas a API do Gmail:
 1. Possuir uma conta Google com Gmail ativado;
 2. Criar um projeto do Google Cloud Platform com a API ativada https://developers.google.com/workspace/guides/create-project;
 3. Autorizar credenciais para aplicação Desktop https://developers.google.com/workspace/guides/create-credentials.

### Executar o projeto
```py .\read_email_messages.py```
