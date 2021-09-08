## Step 2 - MongoDB and Flask Application
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped 
#   from the URLs in 'scrape_mars.py'.
# Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing 
    # document each time the `/scrape` url is visited and new data is obtained.

# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_facts")

# Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

# Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
    # Store the return value in Mongo as a Python dictionary.
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True) 