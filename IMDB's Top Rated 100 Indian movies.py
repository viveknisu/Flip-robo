#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/?sort=ir,desc&mode=simple&page=1')
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[4]:


print(soup.prettify)


# # movie namelist

# In[5]:


name=soup.find_all('td',class_='titleColumn')
name


# In[6]:


movie_name=[]
for i in name:
    movie_name.append(i.text.replace('\n',''))
movie_name


# # IMDB Ratings

# In[7]:


rating=soup.find_all('td',class_="ratingColumn imdbRating")
rating


# In[8]:


IMDB_rating=[]
for i in rating:
    IMDB_rating.append(i.text.replace('\n',' '))
IMDB_rating


# # year of release

# In[9]:


year=soup.find_all('span',class_="secondaryInfo")
year


# In[10]:


year_of_release=[]
for i in year:
    year_of_release.append(i.text.replace('\n',''))
year_of_release


# In[11]:


import pandas as pd


# In[12]:


Top_Rated_100_Indian_movies=pd.DataFrame({})
Top_Rated_100_Indian_movies['movies_name']=movie_name
Top_Rated_100_Indian_movies['IMDB rating']=IMDB_rating
Top_Rated_100_Indian_movies['Year of release']=year_of_release


# In[13]:


Top_Rated_100_Indian_movies


# In[15]:


df2=Top_Rated_100_Indian_movies.iloc[0:100]
df2


# In[ ]:


csv_data=df2.to_csv('csv_data.csv'index=True)

