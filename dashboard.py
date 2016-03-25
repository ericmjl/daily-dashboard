from flask import Flask, render_template
from geopy.geocoders import Nominatim
import forecastio as fc
import os
from datetime import datetime
import json

app = Flask(__name__)

config_path = os.path.join(os.environ['HOME'], '.daily-dashboard')

with open(config_path) as f:
    config = json.load(f)

api_key = config['api_key']
geolocator = Nominatim()
location = geolocator.geocode("60 Wadsworth Street, Cambridge, MA")
lon, lat = location.longitude, location.latitude
curr_time = datetime.now()

forecast = fc.load_forecast(api_key, lat, lon, time=curr_time, units='si')


@app.route('/')
def home():

    return render_template('index.html', forecast=forecast)


if __name__ == '__main__':
    app.run(debug=True)
