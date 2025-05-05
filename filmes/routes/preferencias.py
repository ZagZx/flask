from flask import Blueprint, render_template, make_response, request

pref_route = Blueprint('preferencias', __name__)

@pref_route.route('/')
def pref_page():
    # response = make_response()
    # response.set_cookie('nome', request.args.get('nome'))
    # response.set_cookie('genero', request.args.get('genero'))
    # response.set_cookie('notificacoes', request.args.get('notificacoes'))
    
    return render_template('preferencias.html')

