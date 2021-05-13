#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page=requests.get('https://forecast.weather.gov/MapClick.php?textField1=37.78&textField2=-122.42#.YJgAmofivIU')
page


# In[3]:


page.content


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


soup.prettify


# In[6]:


#period
p=soup.find_all('p', class_="period-name")
p


# In[7]:


Period=[]
for i in p:
    Period.append(i.text.replace('\n',''))
Period


# In[8]:


len(Period)


# In[9]:


#description
dec=soup.find_all('div', class_="col-sm-10 forecast-text")
dec


# In[10]:


short_description=[]
for i in dec:
    short_description.append(i.text.replace('\n',''))
short_description
    


# In[11]:


len(short_description)


# In[12]:


short_desc=short_description[0:9]
short_desc


# In[13]:


len(short_desc)


# In[14]:


#temprature and Description
temp=soup.find_all('p', class_="temp temp-low")
temp


# In[15]:


TEMP_DESC=[]
for i in temp:
    TEMP_DESC.append(i.text.replace('\n',''))
TEMP_DESC


# In[16]:


len(TEMP_DESC)


# In[17]:


#HEIGH TEMP_DESCRICTION
t=soup.find_all('p', class_="temp temp-high")
t


# In[18]:


HEIG_TEMP_DESC=[]
for i in t:
    HEIG_TEMP_DESC.append(i.text.replace('\n',''))
HEIG_TEMP_DESC

# Merge two lists alternatively for temp and Description
# In[19]:


import itertools
from itertools import chain, zip_longest
cl=[x for x in itertools.chain.from_iterable(itertools.zip_longest(TEMP_DESC,HEIG_TEMP_DESC))if x]
cl


# In[20]:


len(cl)


# # Create Data Frame

# # Extended Forecast for San Francisco CA
# 

# In[21]:


import pandas as pd
df=pd.DataFrame({})
df['PERIOD']=Period
df['Short_description']=short_desc
df['Temaprature and description']=cl
df


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




