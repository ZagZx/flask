from app import create_app

app = create_app(drop_tables=True) # não tá funcionando, acho que tá pegando direto do init e não tá rodando o app.py

# se for dropar as tabelas tem que trocar pra true nos parametros da função create_app no __init__