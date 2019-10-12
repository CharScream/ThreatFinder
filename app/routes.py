from flask import render_template,request
from app import app, breaker, teamparser


# @app.before_first_request():

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        team = request.form['team']
        return render_template('result.html', team=team)
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method != 'POST':
        return render_template('index.html')
    assert(request.method != 'GET')
    team = request.form['team']
    input_team = request.form["team"]
    input_team = teamparser.parse(input_team)
    breaker.smash(input_team)

    return render_template('result.html', team=input_team)

# app.run('127.0.0.1', debug=True)
