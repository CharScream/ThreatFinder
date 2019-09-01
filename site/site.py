from flask import Flask, request, render_template
import breaker
import teamparser
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team = request.form['team']
        return render_template('result.html', team=team)
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        team = request.form['team']
        # call python code here on team
        input_team = request.form["team"]
        teamparser.parse(input_team)
        return render_template('result.html', team=input_team)
    return render_template('index.html')


@app.route('/hehe/<name>')
def hehe(name):
    return "sasjkfjksd" + name + '!'


app.run('127.0.0.1', debug=True)
