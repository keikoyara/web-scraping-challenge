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
    
    mars = mongo.db.collection.find_one()

    return render_template('index.html', mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)