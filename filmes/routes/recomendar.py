from flask import Blueprint, render_template

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
    return render_template('')