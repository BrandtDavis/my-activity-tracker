from app import app
import pandas as pd
import pymongo
from flask import render_template, request, jsonify
from database.AthleteQueries import save_athlete, get_athlete_by_id, get_athlete_by_email, delete_athlete_by_id, get_athlete_activities
from utils.timeUtils import get_grouped_activities

import json

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
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/athlete_activities", methods=["GET"])
def athlete_activities():
    athlete_id = request.args["athlete_id"]
    data = get_grouped_activities(int(athlete_id))
    date_keys = data.keys()

    activities_data = []
    for date in date_keys:
        # print(data[date][0])
        # activities = json.loads(data[date][0])
        for activity in data[date][0]:
            print(activity)
            if len(activities_data) == 8:
                break 

            if activity == '':
                activities_data.append(
                    {
                        "week": date,
                        "distance": 0,
                        "date": date,
                    }
                )
                continue

            activity = json.loads(activity)
            
            activities_data.append(
                {
                    "week": date,
                    "distance": activity["distance"],
                    "date": activity["start_date"]
                }
            ) 
            
    response = jsonify(
        {
            'status': 200,
            'message': "success",
            'activities': activities_data
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
