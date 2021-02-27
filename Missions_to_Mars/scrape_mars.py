from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
    browser = Browser('chrome', **executable_path, headless=False)


    mars_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_url)

    #slow down code running
    browser.is_element_present_by_id("at4-thankyou",wait_time=2

    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")


    #finding title 
    mars_title = news_soup.select_one('li.slide').find("div", class_ = "content_title").get_text()
    mars_title


    #finding paragraph 
    mars_paragraph = news_soup.select_one('li.slide').find("div", class_ = "article_teaser_body").get_text()
    mars_paragraph


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
    browser = Browser('chrome', **executable_path)

    jpl_url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(jpl_url)
    #slow down site
    browser.is_element_present_by_id("__nuxt",wait_time=2)


    #Parse Results HTML with BeautifulSoup
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")

    image_url = image_soup.select_one ("img.BaseImage").get("data-src")

    image_url

    browser.visit(image_url)


    mars_facts = pd.read_html("https://space-facts.com/mars/")[0]
    mars_facts.columns=["Properties", "Mars"]
    mars_facts


    # visit USGS website
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
    browser = Browser('chrome', **executable_path, headless=False)

    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    #slow down site
    browser.is_element_present_by_id("results",wait_time=2)


    #create a list to hold urls
    image_urls = []


    #get link for each image 
    image_link = browser.find_by_css("a.product-item h3")
    for i in range(len(image_link)):
        hemisphere = {}
        
        #find element on each loop
        browser.find_by_css("a.itemLink h3")[i].click()
        
        #find sample element and pull href
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
        
        #get hemisphere title
        hemisphere["title"] = browser.find_by_css("h2.title").text
        
        #append to url list
        image_urls.append(hemisphere)
        
        browser.back() 
    
    image_urls

browser.quit()

scraping_components = {
    "mars_news": {"title" : mars_title, "paragraph": mars_paragraph},
    "jpl_image": image_url,
    "facts": mars_facts,
    "hemisphere_image_urls": image_urls
}

return scraping_components

