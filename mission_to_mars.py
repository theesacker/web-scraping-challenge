import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from pprint import pprint

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    #Scrape page with soup
    html = browser.html
    soup = bs(html, "html.parser")

    #get news title
    title_group = soup.find("div", class_="image_and_description_container").find(class_="content_title").text.strip()
    print(title_group)
    news_title = title_group
    #get news paragraph
    paragraph = soup.find("div", class_="image_and_description_container").find(class_="article_teaser_body").text.strip()
    # print(paragraph)
    news_p= paragraph

    #Quit browser
    browser.quit()

    #Grab image from second website
    browser = init_browser()

    url= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    time.sleep(1)
    
    #Scrape page with soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    #get image:
    img = soup.find("a", class_="button fancybox")
    image_url = img["data-fancybox-href"]
    featured_image_url = f"https://www.jpl.nasa.gov/{image_url}"
    print(featured_image_url)

    #Quit browser
    browser.quit()

    # Get Mars Facts
    browser = init_browser()

    url = "https://space-facts.com/mars/"
    browser.visit(url)
    
    time.sleep(1)
    
    #Scrape page with soup
    html = browser.html
    soup = bs(html, "html.parser")

    #get table
    tbl = soup.find("table", class_="tablepress tablepress-id-p-mars").text.split()
    pprint(tbl)

    #Quit browser
    browser.quit()

    # Get hemisphere photos
    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    #Scrape page with soup
    html = browser.html
    soup = bs(html, "html.parser")

    results = soup.find_all("div", class_= "item")
    # img_url = results.find("src")
    # pprint(results)

    for result in results:
        title = result.find("h3").text
        # img_list = result.find("a", class_= "itemLink product-item")
        img_url_link = result.a["href"]
        img_url = f"https://astrogeology.usgs.gov/{img_url_link}"

        print(title)
        print(img_url)
        print("____")

    #Quit browser
    browser.quit()
    
print(scrape_info())

