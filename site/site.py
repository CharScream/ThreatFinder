from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team = request.form['team']
        return render_template('result.html', team=team)
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        team = request.form['team']
        return render_template('result.html', team=team)
    return render_template('Form.html')


app.run('127.0.0.1', debug=True)
