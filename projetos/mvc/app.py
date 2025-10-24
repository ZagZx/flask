from flask import Flask
from extensions import login_manager

app = Flask(__name__)

login_manager.init_app(app)
