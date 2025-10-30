from flask import Flask, render_template
from mvc.extensions import login_manager, init_db


app = Flask(__name__)

login_manager.init_app(app)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

from mvc.controllers import user_bp

app.register_blueprint(user_bp)