from flask import Blueprint, render_template, request

recomendar_route = Blueprint('recomendar', __name__)

@recomendar_route.route('/')
def recomendar_page():
    filmes = {
        "Ação": [
            "Vingadores: Ultimato", 
            "Mad Max: Estrada da Fúria", 
            "John Wick", 
            "Duro de Matar", 
            "Gladiador"
        ],
        "Comédia": [
            "O Máskara", 
            "Superbad - É Hoje", 
            "A Mulher Invisível", 
            "As Branquelas", 
            "Apertem os Cintos... O Piloto Sumiu!"
        ],
        "Drama": [
            "A Espera de um Milagre", 
            "O Poderoso Chefão", 
            "Forrest Gump", 
            "Os 12 Macacos", 
            "O Clube da Luta"
        ],
        "Ficção": [
            "Interestelar", 
            "Blade Runner 2049", 
            "Matrix", 
            "2001: Uma Odisseia no Espaço", 
            "Star Wars: Uma Nova Esperança"
        ],
        "Terror": [
            "O Iluminado", 
            "Hereditary", 
            "A Noite dos Mortos-Vivos", 
            "Atividade Paranormal", 
            "Invocação do Mal"
        ]
    }
    recomendacoes = None
    genero = None

    if not request.args: # pagina recomendar/, sem string de consulta
        genero = request.cookies.get('genero')

    else: # depois de selecionar o formulário
        genero = request.args.get('genero')
        if genero == 'favorito':
            genero = request.cookies.get('genero')
        recomendacoes = filmes[genero]
    return render_template('recomendacoes.html', recomendacoes = recomendacoes, favorito=genero)