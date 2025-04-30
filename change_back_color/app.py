from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/background', methods = ['GET', 'POST'])
def background():
    cor = ''
    if request.method == 'POST':
        cor = request.form['cor']
    return render_template('background.html', cor = cor)

if __name__ == '__main__':
    app.run(debug=True)