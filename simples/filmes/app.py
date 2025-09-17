from flask import Flask

from routes.home import home_route
from routes.cadastro import cadastro_route
from routes.preferencias import pref_route
from routes.cookies import cookies_route
from routes.recomendar import recomendar_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(cadastro_route, url_prefix='/cadastro')
app.register_blueprint(pref_route, url_prefix='/preferencias')
app.register_blueprint(cookies_route, url_prefix='/cookies')
app.register_blueprint(recomendar_route, url_prefix='/recomendar')

if __name__ == '__main__':
    app.run(debug=True)