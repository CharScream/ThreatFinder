from flask import render_template, request
from app import app, breaker, teamparser

RESULT_PAGE = 'result.html'
INDEX_PAGE = 'index.html'


# @app.before_first_request():

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method != 'POST':
        return render_template(INDEX_PAGE, team="""
Try this sample input below!

Groudon @ Red Orb
Ability: Drought
EVs: 144 HP / 156 Atk / 56 SpD / 152 Spe
Adamant Nature
- Stealth Rock
- Swords Dance
- Precipice Blades
- Rock Tomb

Ho-Oh @ Leftovers
Ability: Regenerator
EVs: 252 HP / 204 Def / 52 SpD
Impish Nature
- Sacred Fire
- Recover
- Toxic
- Defog

Kyogre @ Blue Orb
Ability: Drizzle
EVs: 4 Def / 252 SpA / 252 Spe
Modest Nature
- Water Spout
- Calm Mind
- Origin Pulse
- Ice Beam

Rayquaza @ Life Orb
Ability: Air Lock
EVs: 252 Atk / 4 Def / 252 Spe
Adamant Nature
- Dragon Ascent
- Dragon Dance
- Extreme Speed
- Earthquake

Xerneas @ Choice Scarf
Ability: Fairy Aura
EVs: 4 Def / 252 SpA / 252 Spe
Modest Nature
- Moonblast
- Focus Blast
- Aromatherapy
- Defog

Arceus-Rock @ Stone Plate
Ability: Multitype
EVs: 252 HP / 16 Def / 144 SpA / 96 Spe
Timid Nature
- Judgment
- Will-O-Wisp
- Recover
- Stealth Rock""")

    team = request.form['team']
    return render_template(RESULT_PAGE, team=team)


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method != 'POST':
        return render_template(INDEX_PAGE)

    team = request.form['team']
    input_team = request.form["team"]
    input_team = teamparser.parse(input_team)
    if not len(input_team):
        return render_template(INDEX_PAGE, team="Incorrect Input Format, Please Try Again")
    threats = breaker.smash(input_team)
    return render_template(RESULT_PAGE, team=input_team, threats=threats)


app.run('127.0.0.1', debug=True)
