#!/usr/bin/env python
# coding: utf-8

# In[23]:


#importing the trequire libaries
import selenium
import pandas as pd
from selenium import webdriver


# In[24]:


# connect to chrome driver
driver=webdriver.Chrome("chromedriver.exe")
driver


# In[25]:


#opening the the page from nauki.com
driver.get("https://www.naukri.com/")
user_input=input("Enter the text") #ask user to enter the object the job titel,desiganation,skills.etc he or she want to search


# In[26]:


searchbar=driver.find_element_by_id('qsb-keyword-sugg')#webelement for the search bar by ID function 
searchbar.clear()
searchbar.send_keys(user_input)


# In[27]:


location_input=input("Enter the loaction ")#ask user to enter the job loaction where he or she want to search job.
loacation_searchbar=driver.find_element_by_id("qsb-location-sugg")#webelement for Location bar by ID function
loacation_searchbar.clear()
loacation_searchbar.send_keys(location_input)


# In[28]:


#web element for thr search button by xpath function
driver.find_element_by_xpath("//div[@class='search-btn']").click()


# In[29]:


Job_title=[]
Job_location=[]
company_name=[]
experience_required=[]


# In[30]:


for i in range(1,2):
    for t in driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']"): #webelement for the Job Title by xpath function
        Job_title.append(t.text.replace('\n',''))
        
    for j in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']//span"):  #webelement for the Job Location by xpath function
            Job_location.append (j.text.replace('\n',''))
            
    for c in driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']"): #webelement for the Company name by xpath function
          company_name.append(c.text.replace('\n',''))
    for e in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']//span"): #webelement for the experience required by xpath function
        experience_required.append(e.text.replace('\n',''))
    driver.find_element_by_xpath("//a[@class='fright fs14 btn-secondary br2']").click()


# In[31]:


Job_title


# In[32]:


Job_location


# In[33]:


company_name


# In[34]:


experience_required


# In[35]:


#checking the length of each columns
print(len(Job_title),len(Job_location),len(company_name),len(experience_required))


# In[36]:


df=pd.DataFrame({})
df['Job_title']=Job_title
df['Job_location']=Job_location
df['company_name']=company_name
df['experience_required']=experience_required
df


# # top 10 Job Data

# In[37]:


df.iloc[0:10]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




