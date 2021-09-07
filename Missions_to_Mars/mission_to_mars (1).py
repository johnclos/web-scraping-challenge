# dependencies BeautifulSoup, Pandas, and Requests/Splinter
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pymongo
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News
# Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.
    # Assign the text to variables that you can reference later.
url_mars_news = 'https://redplanetscience.com/'
browser.visit(url_mars_news)
html_mars_news = browser.html

# Use BeautifulSoup to help find and parse out the necessary data.  Use either html.parser or lxml parser.
# Create a Beautiful Soup object
soup_mars_news = bs(html_mars_news, 'html.parser')

# Collect the latest News Title and Paragraph Text.
list_text_list = soup_mars_news.find_all('div', class_='list_text')

content_title_strip_list = []
article_teaser_body_strip_list = []

# Loop through returned results (from 12-2-04)
for result in list_text_list:
    
    # Retrieve the title
    content_title = result.find('div', class_='content_title')
    content_title_strip = content_title.text.lstrip()
    content_title_strip_list.append(content_title_strip)
    
    # Retrieve the article body
    article_teaser_body = result.find('div', class_='article_teaser_body')
    article_teaser_body_strip = article_teaser_body.text.lstrip()
    article_teaser_body_strip_list.append(article_teaser_body_strip)


# ### JPL Mars Space Images - Featured Image
# Visit the url for the Featured Space Image site [here](https://spaceimages-mars.com).
url_mars_imag = 'https://spaceimages-mars.com'
browser.visit(url_mars_imag)
html_mars_imag = browser.html

# Use BeautifulSoup to help find and parse out the necessary data.  Use either html.parser or lxml parser.
# Create a Beautiful Soup object
soup_mars_imag = bs(html_mars_imag, 'html.parser')

# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url 
    # string to a variable called `featured_image_url`.  Make sure to find the image url to the full size `.jpg` image.
    # reference C:\Users\jjel0\OneDrive\class_repo\gt-virt-atl-data-pt-06-2021-u-c-2\12-Web-Scraping-and-Document-Databases\2\Activities\07-Ins_Splinter
    # Example:
        # featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'

        # Collect the latest News Title and Paragraph Text.
featured_image = soup_mars_imag.find('a', class_='showimg fancybox-thumbs')
href = featured_image['href']
featured_image_url = 'https://spaceimages-mars.com/' + href


# ### Mars Facts
# Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing
    # facts about the planet including Diameter, Mass, etc.
url_mars_facts = 'https://galaxyfacts-mars.com'
browser.visit(url_mars_facts)
html_mars_facts = browser.html

# Create a Beautiful Soup object
soup_mars_facts = bs(html_mars_facts, 'lxml')

# Use Pandas to convert the data to a HTML table string.
html_mars_facts_df = pd.read_html(url_mars_facts)
html_mars_facts_df


# ### Mars Hemispheres
# Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of 
    # Mars hemispheres.
url_mars_hemis = 'https://marshemispheres.com/'
browser.visit(url_mars_hemis)
html_mars_hemis = browser.html

# Use BeautifulSoup to help find and parse out the necessary data.  Use either html.parser or lxml parser.
# Create a Beautiful Soup object
soup_mars_hemis = bs(html_mars_hemis, 'html.parser')

# Print the image links
hemis_url_list = soup_mars_hemis.find_all('a', class_='itemLink product-item')

content_title_hemis_list = []
hemis_image_url_list = []
# Loop through returned results
for result in hemis_url_list:
    
    # Retrieve the title
    content_title = result.find('h3')
    content_title_hemis_list.append(content_title)
    
    # Retrieve the images of the hemisphers
    hemis_image = soup_mars_hemis.find('a', class_='itemLink product-item')
    href = result['href']
    hemis_image_url = 'https://marshemispheres.com/' + href
#     print(hemis_image_url)
    hemis_image_url_list.append(hemis_image_url)

Not_none_values = filter(None.__ne__, content_title_hemis_list)

content_title_hemis_listvalues = list(Not_none_values)

hemis_image_url_list

# You will need to click each of the links to the hemispheres in order to find the image url to the full
    # resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing
    # the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain
    # one dictionary for each hemisphere.
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
]