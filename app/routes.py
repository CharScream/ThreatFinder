from flask import render_template,request #Flask,  
from app import app, breaker, teamparser
# import breaker
# import teamparser


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
        input_team = teamparser.parse(input_team)
        breaker.smash(input_team)


        return render_template('result.html', team=input_team)
    return render_template('index.html')


@app.route('/hehe/<name>')
def hehe(name):
    return "sasjkfjksd" + name + '!'


# app.run('127.0.0.1', debug=True)
