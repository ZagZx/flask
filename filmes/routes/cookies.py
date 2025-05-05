from flask import Blueprint, request, make_response, url_for,redirect

cookies_route = Blueprint('cookies', __name__)

@cookies_route.route('/salvar-preferencias', methods = ['POST'])
def salvar_preferencias():
    response = make_response(redirect(url_for('preferencias.pref_page')))
    response.set_cookie('nome', request.form['nome'])
    response.set_cookie('genero', request.form['genero'])
    response.set_cookie('notificacoes', request.form['notificacoes'])

    return response