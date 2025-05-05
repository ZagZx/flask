from flask import Blueprint, render_template, request

recomendar_route = Blueprint('recomendar', __name__)

@recomendar_route.route('/')
def recomendar_page():
    filmes = {
        "acao": [
            "Vingadores: Ultimato", 
            "Mad Max: Estrada da Fúria", 
            "John Wick", 
            "Duro de Matar", 
            "Gladiador"
        ],
        "comedia": [
            "O Máskara", 
            "Superbad - É Hoje", 
            "A Mulher Invisível", 
            "As Branquelas", 
            "Apertem os Cintos... O Piloto Sumiu!"
        ],
        "drama": [
            "A Espera de um Milagre", 
            "O Poderoso Chefão", 
            "Forrest Gump", 
            "Os 12 Macacos", 
            "O Clube da Luta"
        ],
        "ficcao": [
            "Interestelar", 
            "Blade Runner 2049", 
            "Matrix", 
            "2001: Uma Odisseia no Espaço", 
            "Star Wars: Uma Nova Esperança"
        ],
        "terror": [
            "O Iluminado", 
            "Hereditary", 
            "A Noite dos Mortos-Vivos", 
            "Atividade Paranormal", 
            "Invocação do Mal"
        ]
    }
    acentuacao = {
        'acao': 'Ação',
        'terror': 'Terror',
        'ficcao': 'Ficção',
        'comedia': 'Comédia',
        'drama': 'Drama'
    }
    recomendacoes = None
    genero_tratado = None

    if request.args:
        genero = request.args.get('genero')
        recomendacoes = filmes[genero]
        genero_tratado = acentuacao[genero]

    return render_template('recomendacoes.html', recomendacoes = recomendacoes, traducao = genero_tratado)