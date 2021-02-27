from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape

#create instance of Flask app
app = Flask(__name__)

#connect to mongo db 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#flask routes 
@app.route("/")
def home():
    # creating an object of the mars data
    mars_data = mongo.db.mars_info.find_one()

    # using render template to send bits of mars data to html template
    return render_template(
        'index.html', 
        
        )