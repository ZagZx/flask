## Integrantes
- Pedro Victor Dantas Azevedo
- Pedro Victor Dantas Azevedo
- Pedro Victor Dantas Azevedo
- Pedro Victor Dantas Azevedo

## Dependências
- Python
- MySQL

## Instruções
**Todos os passos adiante devem ser realizados na pasta raiz do projeto** (loja/)

<details>
  <summary>Linux</summary>
    
  - **Criando o virtual environment:**
     ```bash
     python3 -m venv venv
     ```
  - **Ativando o virtual environment:**
     ```bash
     source venv/bin/activate
     ```
  - **Instalando dependências:**
     ```bash
     pip install -r requirements.txt
     ```
  - **Iniciando o servidor:**
     ```bash
     flask run
     ```
</details>

<details>
  <summary>Windows</summary>
    
  - **Criando o virtual environment:**
     ```bash
     python -m venv venv
     ```
  - **Ativando a virtual environment:**

    CMD:
     ```bash
     .\venv\Scripts\activate
     ```
    PowerShell:
     ```bash
     .\venv\Scripts\activate.ps1
     ```
  - **Instalando dependências:**
     ```bash
     pip install -r requirements.txt
     ```
  - **Iniciando o servidor:**
     ```bash
     flask run
     ```
</details>

## Observações
- Usuário root não pode ter senha
- O código cria o banco automaticamente
- Não testei no windows ainda
