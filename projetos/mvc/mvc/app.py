from flask import Flask, render_template
from mvc.extensions import login_manager, init_db
from mvc.config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager.init_app(app)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

from mvc.controllers import user_bp

app.register_blueprint(user_bp)