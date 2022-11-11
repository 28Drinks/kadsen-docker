from collections import defaultdict
from unittest import result
from my_project import app
from flask import render_template, jsonify, request
from my_project import db

from datetime import datetime, timedelta
import json

@app.route("/reveal")
def whats_left():

    with open('whats-left.json') as f:
        result = json.load(f)

    trait_types = ["Background","Eyes","Teeth","Body"]

    total_left = 0
    total_eye_worth = 0
    total_teeth_worth = 0
    total_body_worth = 0
    total_background_worth = 0
    x = 0
    for e in result["Eyes"]:
        x += 1
        left = result["Eyes"].get(e)[2]
        total_left += left

        eye_value = result["Eyes"].get(e)[3]
        eye_worth = left * eye_value
        total_eye_worth += eye_worth

    for b in result["Background"]:
        background_value = result["Background"].get(b)[3]
        left = result["Background"].get(b)[2]
        background_worth = left * background_value
        total_background_worth += background_worth

    for t in result["Teeth"]:
        teeth_value = result["Teeth"].get(t)[3]
        left = result["Teeth"].get(t)[2]
        teeth_worth = left * teeth_value
        total_teeth_worth += teeth_worth


    for bo in result["Body"]:
        body_value = result["Body"].get(bo)[3]
        left = result["Body"].get(bo)[2]
        body_worth = left * body_value
        total_body_worth += body_worth

    print(total_left,total_background_worth,total_eye_worth,total_teeth_worth,total_body_worth)

    return render_template("reveal.html",pagetitle="un-revealed", trait_types=trait_types,result=result,total_background_worth=total_background_worth,total_body_worth=total_body_worth,total_eye_worth=total_eye_worth,total_teeth_worth=total_teeth_worth,total_left=total_left)