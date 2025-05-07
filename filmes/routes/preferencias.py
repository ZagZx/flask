from flask import Blueprint, render_template, request

pref_route = Blueprint('preferencias', __name__)

@pref_route.route('/')
def pref_page():
    nome = request.cookies.get('nome')
    genero = request.cookies.get('genero')
    notificacoes = request.cookies.get('notificacoes')
    
    return render_template('preferencias.html', nome = nome, genero = genero, notificacoes = notificacoes)

