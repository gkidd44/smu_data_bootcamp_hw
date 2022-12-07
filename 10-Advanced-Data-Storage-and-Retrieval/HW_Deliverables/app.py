# Code structure and elements borrowed from the instructor's example materials during the lecture. 
# This Python script is establishing a Flask API with custom routes where a user can query a database 
# based on pre-defined SQL queries, and recieve data back within a browser as JSON. 

from flask import Flask, jsonify
import pandas as pd
from sqlHelper import SQLHelper

# Flask Setup

app = Flask(__name__)
sqlHelper = SQLHelper()

# Flask Routes

@app.route("/")
def home():
    return ("""<xmp>
        Welcome to the Garrett's SMU HW10 Climate API!

        Here are the possible routes to go:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/<start>    (put in a date for <start> in the format 2015-09-21)
        /api/v1.0/<start>/<end>    (put in dates for <start> and <end> in the format 2015-09-21)
        </xmp>""")


@app.route("/api/v1.0/precipitation")
def get_precip():
    df = sqlHelper.get_precip()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_stations():
    df = sqlHelper.get_stations()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/tobs")
def get_tobs():
    df = sqlHelper.get_tobs()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def specified_start(start):
    df = sqlHelper.specified_start(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def start_and_end(start, end):
    df = sqlHelper.start_and_end(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == "__main__":
    app.run(debug=True)
