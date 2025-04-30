# Criar uma aplicação que tenha uma página com um formulário.

#     Esse formulário recebe 2 números
#     Soma os números
#     Retorna: 'A soma é: XXX'

from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/numero')
def numero():
    soma = int(request.args.get('num1')) + int(request.args.get('num2'))
    return f'A soma é {soma}'