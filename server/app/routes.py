from app import app
from flask import render_template, request, jsonify
from database.AthleteQueries import save_athlete, get_athlete_by_id, delete_athlete_by_id


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/userDetails")
def user_details():
    # return get_athlete_by_id(95573308)
    return {'name': 'Brandt'}

@app.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]

    if email == "user" and password == "pass":
        response = jsonify({'status': 200, 'message':"Great success"})
        return response
