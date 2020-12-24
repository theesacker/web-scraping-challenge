from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create instance of Flask
app = Flask(__name__)

#Create PyMongo Connection 
mongo = PyMongo(app,uri="mongodb://localhost:27017")
collection = mongo.db.destination

#Route to render to html
@app.route("/")
def index():

    #Find record of data from Mongo database
    mars_data = mongo.db.collection.find_one()
    print(mars_data)

    # Return template and data
    return render_template("index.html", mars=mars_data)

# Route that will trigger scrape
@pp.route("/scrape")
def scrape():
    
    #call scrape function from mission to mars Py
    planet_data = mission_to_mars.scrape_info()

    # Update Mongo Db using upsert = True
    collection.update({}, planet_data, upsert=True)

    # Redirect to Home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
