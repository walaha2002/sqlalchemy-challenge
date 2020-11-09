import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
# base.classes.keys()

# Save references to each table
measurement = base.classes.measurement
station=base.classes.station

# Create an app
app=Flask(__name__)

# Define static routes
@app.route("/")
def index():
    print("Server received request from home page...")
    return ("Precipitation and Temperatures of Hawaii Stations<br/><br/>"
    "     Available routes are the following:<br/><br/>"
    "     Precipitation: /api/v1.0/precipitation<br/><br/>"
    "     Stations: /api/v1.0/stations<br/><br/>"
    "     Start Dates: /api/v1.0/<start><br/><br/>"
    "     Start and End Dates: /api/v1.0/<start>/<end><br/><br/>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    

    #Query dates and precipitation
    dates_prcp=session.query(measurement.date,measurement.prcp).all()

    session.close()

    prcp_list=[]
    for date, prcp in dates_prcp:
        prcp_dict={}
        prcp_dict[date]=prcp
        # prcp_dict["prcp"]=prcp
        prcp_list.append(prcp_dict)
    
    return jsonify(prcp_list)

   
# @app.route("/api/v1.0/stations/<station>)
@app.route("/api/v1.0/tobs")
def tobs():
     # Create our session (link) from Python to the DB
    session = Session(engine)

      #Query dates and precipitation
    stations=session.query(station.station,station.name,station.latitude,station.longitude,station.elevation).all()

    session.close()

    return jsonify(stations)

if __name__=="__main__":
    app.run(debug=True)