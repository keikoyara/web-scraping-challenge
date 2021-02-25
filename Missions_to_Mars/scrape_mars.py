#!/usr/bin/env python
# coding: utf-8

# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


get_ipython().system('which chromedriver')


# # Step 1 Scraping
# 

# ### NASA Mars News
# 
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 
# Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# In[4]:


#setup splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
browser = Browser('chrome', **executable_path, headless=False)


# In[5]:


mars_url = 'https://mars.nasa.gov/news/'
browser.visit(mars_url)


# In[6]:


#slow down code running
browser.is_element_present_by_id("at4-thankyou",wait_time=2)


# In[7]:


#Parse Results HTML with BeautifulSoup
html = browser.html
news_soup = BeautifulSoup(html, "html.parser")


# In[8]:


#finding title 
#anything scraping needs to be in quotes
mars_title = news_soup.select_one('li.slide').find("div", class_ = "content_title").get_text()
mars_title


# In[9]:


#finding paragraph 
mars_paragraph = news_soup.select_one('li.slide').find("div", class_ = "article_teaser_body").get_text()
mars_paragraph


# ### JPL Mars Space Images - Featured Image
# Visit the url for JPL Featured Space Image.
# 
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# 
# Make sure to find the image url to the full size .jpg image.
# 
# 
# Make sure to save a complete url string for this image.
# 
# 
# Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

# In[10]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
browser = Browser('chrome', **executable_path)


# In[11]:


jpl_url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
browser.visit(jpl_url)


# In[12]:


#slow down site
browser.is_element_present_by_id("__nuxt",wait_time=2)


# In[13]:


#Parse Results HTML with BeautifulSoup
html = browser.html
image_soup = BeautifulSoup(html, "html.parser")

image_url = image_soup.select_one ("img.BaseImage").get("data-src")

image_url


# In[14]:


browser.visit(image_url)


# ### Mars Facts
# 
# 
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# 
# 
# Use Pandas to convert the data to a HTML table string.

# In[15]:


mars_facts = pd.read_html("https://space-facts.com/mars/")[0]
mars_facts.columns=["Properties", "Mars"]
mars_facts


# ### Mars Hemispheres
# 
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# 
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# 
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# 
# Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# In[16]:


#hardest part will be scraping images. create an empty list. slow down website. 
#loop url to pull images. find link of image in there first. push to dictionary push to list 


# In[25]:


# visit USGS website
executable_path = {'executable_path': '/usr/local/bin/chromedriver'} 
browser = Browser('chrome', **executable_path, headless=False)


# In[26]:


hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere_url)


# In[29]:


#slow down site
browser.is_element_present_by_id("results",wait_time=2)


# In[30]:


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


# In[31]:


image_urls


# In[ ]:




