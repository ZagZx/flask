from flask import Blueprint, request, make_response, url_for, redirect

cookies_route = Blueprint('cookies', __name__)

@cookies_route.route('/salvar-preferencias', methods = ['POST'])
def salvar_preferencias():
    validade = 7 * 24 * 60 * 60 # 7 dias
    response = make_response(redirect(url_for('preferencias.pref_page')))
    response.set_cookie('notificacoes', 'Não', validade)
    if 'notificacoes' in request.form:
        response.set_cookie('notificacoes', 'Sim', validade)
    if request.form['genero']:
        response.set_cookie('genero', request.form['genero'], validade)

    response.set_cookie('nome', request.form['nome'], validade)
    
    

    return response