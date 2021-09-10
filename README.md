
## Step 1 - Scraping
* In Jupyter Notebook `mission_to_mars.ipynb`:
    * Import dependencies
    * Setup splinter

### NASA Mars News
* Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.
    * Assign the text to variables that you can reference later.
* Use BeautifulSoup to help find and parse out the necessary data.  Use either html.parser or lxml parser.
    * Create a Beautiful Soup object
* Create a dictionary
* Collect the latest News Title and Paragraph Text.
* Retrieve the title and article body.

### JPL Mars Space Images - Featured Image
* Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
* Use BeautifulSoup to help find and parse out the necessary data.  Use either html.parser or lxml parser.
    * Create a Beautiful Soup object
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url 
    * string to a variable called `featured_image_url`.  Make sure to find the image url to the full size `.jpg` image.
    * Example:
        * featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
* Create the image url.

### Mars Facts
* Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing
    * facts about the planet including Diameter, Mass, etc.
* Create a Beautiful Soup object.
* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
* # Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of 
    * Mars hemispheres.
* Create the hemis url list.
* Loop through returned results to create the hemisphere images.

* Close the browser.

### Export 'mission_to_mars.ipynb' as 'scrape_mars.py' and clean up as necessary.

## Step 2 - MongoDB and Flask Application
* In 'app.py':
    * Import necessary libraries
    * create instance of Flask app
    * Use PyMongo to establish Mongo connection
    * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
        * Find one record of data from the mongo database
        * Return template and data
    * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
        * Store the return value in Mongo as a Python dictionary.
        * Run the scrape function
        * Update the Mongo database using update and upsert=True
        * Redirect back to home page

* In 'index.html':
* Take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following
    * as a guide for what the final product should look like, but feel free to create your own design.
        * Mission to Mars
        * Scrape New Data (button to retrieve the scraped data from the dictionary)
    * Create containers for what is returned:
        * Latest Mars News
        * Featured Mars Image
        * Container for Mars Facts table
        * Mars Hemispheres images