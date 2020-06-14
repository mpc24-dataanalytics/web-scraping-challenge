#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time
from selenium import webdriver 
import re


# In[ ]:


### NASA Mars News


# In[ ]:


mars={}


# In[ ]:


#Visit NASA Mars News url to scrape the page
browser=Browser('chrome')
url='https://mars.nasa.gov/news/'
browser.visit(url)

#Parse with 'html.parser'with beautifulsoup object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


#Collect latest news title and paragraph text
news_title= soup.find_all('div', class_= 'content_title')
news_title[1].text


# In[ ]:


news_para=soup.find('div', class_='article_teaser_body').text
news_para


# In[11]:


mars["news_title"]=news_title[1].text
mars["news_para"]=news_para
mars


# In[ ]:


### JPL Mars Space Images


# In[7]:


#Visit JPL featured space image url to scrape the page
browser=Browser('chrome')
url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[8]:


time.sleep(2)
browser.find_by_id('full_image').click()
time.sleep(2)
browser.find_link_by_partial_text('more info').click()

#Parse with 'html.parser'with beautifulsoup object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

link=soup.select_one('figure.lede a img').get('src')
link


# In[9]:


full_link='https://www.jpl.nasa.gov'+link


# In[12]:


mars["featured_image_url"]=full_link
mars


# In[ ]:


### Mars Weather


# In[14]:


#Visit Mars Weather Twitter url to scrape the page
browser=Browser('chrome')
url='https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[21]:


#Parse with 'html.parser'with beautifulsoup object
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

text=re.compile(r'sol')

link=soup.find('span', text=text).text
link


# In[22]:


mars["mars_weather"]=link


# In[31]:


table=pd.read_html('https://space-facts.com/mars/')
df=table [0]
df.columns=["Description", "Value"]
df


# In[33]:


mars['facts']=df.to_html()


# In[34]:


mars


# In[35]:


### Mars Hemispheres


# In[49]:


#Visit USGS Astrogeology url to scrape the page
browser=Browser('chrome')
url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[51]:


#Parse with 'html.parser'with beautifulsoup object
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[52]:


#Create a dictionary to include titles and links for mars hemispheres
hemisphere_urls=[]
products=soup.find ('div', class_='result-list')
hemispheres=products.find_all('div',{'class':'item'})

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html_hemispheres = browser.html
    soup=BeautifulSoup(html_hemispheres, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    hemisphere_urls.append({"title": title, "img_url": image_url})
 


# In[54]:


hemisphere_urls


# In[ ]:




