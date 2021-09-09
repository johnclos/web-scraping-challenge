# dependencies BeautifulSoup, Pandas, and Requests/Splinter
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pymongo
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

data = {}

def scrape_info():
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

    list_text_list = soup_mars_news.find('div', class_='list_text')
    content_title = list_text_list.find('div', class_='content_title').get_text()  
    article_teaser_body = list_text_list.find('div', class_='article_teaser_body').get_text()

    data["news_title"] = content_title
    data["news_paragraph"] = article_teaser_body


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
    featured_image = soup_mars_imag.find('a', class_='showimg fancybox-thumbs')

    href = featured_image['href']
    featured_image_url = 'https://spaceimages-mars.com/' + href
    
    data["featured_image_url"] = featured_image_url


    # ### Mars Facts
    # Visit the Mars Facts webpage [here](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing
        # facts about the planet including Diameter, Mass, etc.
    url_mars_facts = 'https://galaxyfacts-mars.com'
    browser.visit(url_mars_facts)
    html_mars_facts = browser.html

    # Create a Beautiful Soup object
    soup_mars_facts = bs(html_mars_facts, 'lxml')

    # Use Pandas to convert the data to a HTML table string.
    html_mars_facts_html = pd.read_html(url_mars_facts)[1]

    html_mars_facts_html.columns = ["description", "value"]
    data["facts"] = html_mars_facts_html.to_html(index=False)


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
    hemis_url_list

    hemisphere_image_urls = []
    # Loop through returned results
    for i in range(4):
        browser.find_by_css('a.product-item img')[i].click()
        hemisphere = {}
        
        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css('h2.title').text
        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)
        # Finally, we navigate backwards
        browser.back()

    data["hemisphere_image_urls"] =  hemisphere_image_urls

    browser.quit()

    return data