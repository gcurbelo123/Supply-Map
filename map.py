import os
from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import requests
import json
import urllib2

app = Flask(__name__, template_folder = "templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/')
def placeSearch():
    return render_template('placeSearch.html')
    
if __name__ == '__main__':
    app.run(debug = True,
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0')
    )