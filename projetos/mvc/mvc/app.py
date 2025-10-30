from flask import Flask, render_template
from mvc.extensions import login_manager, init_db


app = Flask(__name__)
app.secret_key = 'f3e96343329fbce048277af8b4c880923e273174557c2af7c1bd1017255d1626'

login_manager.init_app(app)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

from mvc.controllers import user_bp

app.register_blueprint(user_bp)