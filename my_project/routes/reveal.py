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

    return render_template("reveal.html",pagetitle="un-revealed", trait_types=trait_types,result=result)