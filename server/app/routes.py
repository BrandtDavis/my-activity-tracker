from app import app
from flask import render_template, request, jsonify
from database.AthleteQueries import save_athlete, get_athlete_by_id, get_athlete_by_email, delete_athlete_by_id

from database.Connection import Connection
conn = Connection()
db = conn.connect()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/athleteInfo", methods=["GET"])
def athlete_info():
    athlete_id = request.args["athlete_id"]
    data = get_athlete_by_id(int(athlete_id))

    response = jsonify(
        {
            'status': 200,
            'message': "Success",
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email']
        }
    )

    return response

@app.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]

    athlete = get_athlete_by_email(email)
    if  athlete != None:
        response = jsonify(
            {
                'status': 200, 
                'message':"Great success",
                # 'auth_token': '',
                'athlete_id': athlete['athlete_id']
            }
        )
        return response
    
    return {'status': 400, 'message':"No success"}
