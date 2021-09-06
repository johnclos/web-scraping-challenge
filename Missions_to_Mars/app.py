## Step 2 - MongoDB and Flask Application
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped 
#   from the URLs in 'scrape_mars.py'.
# Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing 
    # document each time the `/scrape` url is visited and new data is obtained.

# import necessary libraries
from flask import Flask, render_template
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
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)

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




# def index():
#     team_list = ["Jumpers", "Dunkers", "Dribblers", "Passers"]
#     return render_template("index.html", list=team_list)


# def index():
#     player_dictionary = {"player_1": "Jessica",
#                          "player_2": "Mark"}
#     return render_template("index.html", dict=player_dictionary)


# # List of dictionaries
# dogs = [{"name": "Fido", "type": "Lab"},
#         {"name": "Rex", "type": "Collie"},
#         {"name": "Suzzy", "type": "Terrier"},
#         {"name": "Tomato", "type": "Retriever"}]

# # create route that renders index.html template
# @app.route("/")
# def index():

#     return render_template("index.html", dogs=dogs)


# # Drops collection if available to remove duplicates
# db.team.drop()

# # Creates a collection in the database and inserts two documents
# db.team.insert_many(
#     [
#         {
#             'player': 'Jessica',
#             'position': 'Point Guard'
#         },
#         {
#             'player': 'Mark',
#             'position': 'Center'
#         }
#     ]
# )

# # Set route
# @app.route('/')
# def index():
#     # Store the entire team collection in a list
#     teams = list(db.team.find())
#     print(teams)

#     # Return the template with the teams list passed in
#     return render_template('index.html', teams=teams)


# # connect to mongo db and collection
# db = client.store_inventory
# produce = db.produce


# @app.route("/")
# def index():
#     # write a statement that finds all the items in the db and sets it to a variable
#     inventory = list(produce.find())
#     print(inventory)

#     # render an index.html template and pass it the data you retrieved from the database
#     return render_template("index.html", inventory=inventory)



# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
# mongo = PyMongo(app)

# # Or set inline
# # mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


# @app.route("/")
# def index():
#     listings = mongo.db.listings.find_one()
#     return render_template("index.html", listings=listings)


# @app.route("/scrape")
# def scraper():
#     listings = mongo.db.listings
#     listings_data = scrape_phone.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# # Route to render index.html template using data from Mongo
# @app.route("/")
# def home():

#     # Find one record of data from the mongo database
#     destination_data = mongo.db.collection.find_one()

#     # Return template and data
#     return render_template("index.html", vacation=destination_data)

# # Route that will trigger the scrape function
# @app.route("/scrape")
# def scrape():

#     # Run the scrape function
#     costa_data = scrape_costa.scrape_info()

#     # Update the Mongo database using update and upsert=True
#     mongo.db.collection.update({}, costa_data, upsert=True)

#     # Redirect back to home page
#     return redirect("/")