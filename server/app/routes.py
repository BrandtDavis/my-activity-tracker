from app import app
from flask import render_template
from database.AthleteQueries import save_athlete, get_athlete_by_id, delete_athlete_by_id


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/userDetails")
def chungus():
    # return get_athlete_by_id(95573308)
    return {'name': 'Brandt'}