from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ["POST"])
def manda_beck():
    cor = request.form['cor']
    return cor

@app.route('/background')
def background():
    return render_template('background.html')

if __name__ == '__main__':
    app.run(debug=True)