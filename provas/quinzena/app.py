from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return f'''<a href="{ url_for("cadastro") }">Cadastre-se</a>
    <a href="{ url_for("perfil")}">Ver Perfil<a/>'''

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro", methods= ['POST'])
def salvar_cookies():
    response = make_response(redirect(url_for('perfil')))
    response.set_cookie('nome', request.form.get('nome'), 120)
    response.set_cookie('curso', request.form.get('curso'), 120)

    return response

@app.route("/perfil")
def perfil():
    nome = 'Não informado'
    curso = 'Não informado'

    if request.cookies:
        nome = request.cookies.get('nome')
        curso = request.cookies.get('curso')

    if request.args.get('nome'):
        nome = request.args.get('nome')
    if request.args.get('curso'):
        curso = request.args.get('curso')

    return render_template('perfil.html', nome = nome, curso = curso)