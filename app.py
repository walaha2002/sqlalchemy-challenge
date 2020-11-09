# Import Flask
from flask import Flask, jsonify

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

if __name__=="__main__":
    app.run(debug=True)


# @app.route("/api/v1.0/precipitation)
# @app.route("/api/v1.0/stations)
# @app.route("/api/v1.0/tobs)

