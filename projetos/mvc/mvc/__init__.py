from flask import Flask
from mvc.extensions import login_manager, init_db


def create_app() -> Flask:
    app = Flask(__name__)

    login_manager.init_app(app)

    init_db()

    return app