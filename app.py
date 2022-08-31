# import dependencies
import datetime as dt
import pandas as pd

#import sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import flask
from flask import Flask, jsonify

# set up database engine to access and query sqlite db file

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

# reflect the db

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement

Station = Base.classes.station

# Create  a session link from python to db
session = Session(engine)


app = Flask(__name__)

@app.route("/")

def welcome():
    return(    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

app.run(debug=True)


