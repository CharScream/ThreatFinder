from flask import render_template,request
from app import app, breaker, teamparser

RESULT_PAGE = 'result.html'
INDEX_PAGE = 'index.html'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method != 'POST':
        return render_template(INDEX_PAGE)

    team = request.form['team']
    return render_template(RESULT_PAGE, team=team)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method != 'POST':
        return render_template(INDEX_PAGE)

    team = request.form['team']
    input_team = request.form["team"]
    input_team = teamparser.parse(input_team)
    threats = breaker.smash(input_team)
    return render_template(RESULT_PAGE, team=input_team, threats=threats)


# app.run('127.0.0.1', debug=True)
