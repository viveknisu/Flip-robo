#!/usr/bin/env python
# coding: utf-8

# # Data Scrapping 

# # Importing the required libraries:-

# In[1]:


import selenium
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests


# In[2]:


#activating the chrome browser
driver=webdriver.Chrome('chromedriver.exe')
#opening the home page of amazon.in
url="https://www.amazon.in/"
driver.get(url)


# In[3]:


driver.find_element_by_xpath("//div[@class='nav-search-scope nav-sprite']").click()


# In[4]:


#selection the clothing Acessores from drop boxes
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select/option[14]").click()


# # Srcapping the - Sarees (women):

# In[5]:


#web lelemnt for the search box
driver.find_element_by_id('twotabsearchtextbox').send_keys('Sarees')


# In[6]:


#web element for the submit button
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()


# In[7]:


url=[]
for i in range(4):
    for u in driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//img"):
        url.append(u.get_attribute('src'))


# In[8]:


len(url)


# In[9]:


for i in range(len(url)):
    if i  >= 200:
        break
    print("Downloading {0} of {1} images" .format(i, 240))
    response= requests.get(url[i])
    file = open("D:\Data Trained\FlipRobo\prjoect image scrapping sept 14"+str(i)+".jpg", "wb")
    file.write(response.content)
    


# # Srcapping the -	Trousers (men)

# In[10]:


url="https://www.amazon.in/"
driver.get(url)


# In[11]:


driver.find_element_by_xpath("//div[@class='nav-search-scope nav-sprite']").click()


# In[12]:


#selection the clothing Acessores from drop boxes
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select/option[14]").click()


# In[13]:


#web lelemnt for the search box
driver.find_element_by_id('twotabsearchtextbox').send_keys('Trousers')


# In[14]:


#web element for the submit button
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()


# In[15]:


turl=[]
for i in range(4):
    for u in driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//img"):
             turl.append(u.get_attribute('src'))
        
       
    


# In[16]:


len(turl)


# In[17]:


for i in range(len(turl)):
    if i  >= 200:
        break
    print("Downloading {0} of {1} images" .format(i, 240))
    response= requests.get(turl[i])
    file = open("D:\Data Trained\mens"+str(i)+".jpg", "wb")
    file.write(response.content)


# # Srcapping the -Jeans (men):

# In[18]:


url="https://www.amazon.in/"
driver.get(url)


# In[19]:


driver.find_element_by_xpath("//div[@class='nav-search-scope nav-sprite']").click()


# In[20]:


#selection the clothing Acessores from drop boxes
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select/option[14]").click()


# In[21]:


#web lelemnt for the search box
driver.find_element_by_id('twotabsearchtextbox').send_keys('jeans')


# In[22]:


#web element for the submit button
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()


# In[23]:


jurl=[]
for i in range(5):
    for u in driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-tall-aspect']//img"):
             jurl.append(u.get_attribute('src'))
        


# In[24]:


len(jurl)


# In[25]:


for i in range(len(jurl)):
    if i  >= 200:
        break
    print("Downloading {0} of {1} images" .format(i, 240))
    response= requests.get(jurl[i])
    file = open("D:\Data Trained\mens"+str(i)+".jpg", "wb")
    file.write(response.content)
    

