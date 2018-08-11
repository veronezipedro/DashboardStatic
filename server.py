# Import Flask
from flask import Flask, render_template, request
# Import requests library to make call to Accuweather API
import requests
# Import os to get API_KEY which was sourced from secrets.sh
import os

# Import our weather UI helper function!
from weather_ui import get_ui_attributes

# Always keep your API Key secret
# Source secrets.sh file to use API Key
API_KEY = "PBGmITRYnFLrAu33RSuYL5KyWYH4OIyg"

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

##################################
# ROUTING
##################################

# Establish routing for home page.
@app.route('/')
def index():
    """Home page."""

    # Render index page
    return render_template('example.html')

##################################
# Necessary to get application running.
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our
    # web app if we change the code.
    app.run(debug=True, host='0.0.0.0', port=5000)
