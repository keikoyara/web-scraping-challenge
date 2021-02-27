from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create instance of Flask app
app = Flask(__name__)

#connect to mongo db 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



#flask routes 
@app.route("/")
def home():
    # creating an object of the mars data
    mars_data = mongo.db.collection.find_one()

    # using render template to send bits of mars data to html template
    return render_template('index.html', mars=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_mars()

    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)