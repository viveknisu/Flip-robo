#!/usr/bin/env python
# coding: utf-8

# In[47]:


import selenium
import pandas as pd
from selenium import webdriver


# In[48]:


#connect to the chrom
driver=webdriver.Chrome("chromedriver.exe")
driver


# In[49]:


url='https://www.naukri.com/'
driver.get(url)


# In[50]:


#scrap search button
search=driver.find_element_by_id('qsb-keyword-sugg')
search


# In[51]:


search.send_keys('Data Scientist')


# In[52]:


#scrap location buttoon by ID function
Location=driver.find_element_by_id("qsb-location-sugg")
Location


# In[53]:


Location.send_keys('Bangalore')


# In[54]:


#scrap search button vy x path function
searc=driver.find_element_by_xpath("//div[@class='search-btn']")
searc.click()


# In[60]:


#jobtitle by xpath function
Title=[]
title=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for i in title:
    Title.append(i.text)
Title


# In[143]:


Title[0:10]


# In[56]:


#web_element for the comapny name by xpath function 
Company=[]
c_name=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
for i in c_name:
    Company.append(i.text)
Company  


# In[144]:


Company [0:10]


# In[57]:


#web_element for the location by Xpath Function
Lcation=[]
for i in driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']"):
    Lcation.append(i.text)
Lcation   


# In[145]:


Lcation[0:10]


# In[64]:


#full job Description
U_1="https://www.naukri.com/job-listings-data-scientist-data-analyst-business-analyst-inflexion-analytix-private-limited-mumbai-hyderabad-secunderabad-pune-gurgaon-gurugram-chennai-bangalore-bengaluru-0-to-3-years-100521000368?src=jobsearchDesk&sid=16217350952976404&xp=1&px=1"


# In[65]:


driver.get(U_1)


# In[79]:


desc_1=driver.find_element_by_xpath("//div[@class='dang-inner-html']")
x=desc_1.text.replace('\n','')
x


# In[80]:


a=x.split('\n')
a


# In[16]:


U_2='https://www.naukri.com/job-listings-data-scientist-wipro-limited-kolkata-hyderabad-secunderabad-chennai-bangalore-bengaluru-4-to-9-years-210521000038?src=jobsearchDesk&sid=16217371471507128&xp=2&px=1'


# In[17]:


driver.get(U_2)


# In[82]:


desc_2=driver.find_element_by_xpath("//div[@class='dang-inner-html']")
y=desc_2.text.replace('\n','')
y


# In[84]:


b=y.split('\n')
b


# In[87]:


U_3=('https://www.naukri.com/job-listings-big-data-ai-ml-xoriant-solutions-pvt-ltd-kochi-cochin-hyderabad-secunderabad-pune-ahmedabad-bangalore-bengaluru-mumbai-all-areas-1-to-3-years-130521005075?src=jobsearchDesk&sid=16217374629284108&xp=1&px=1')
driver.get(U_3)


# In[89]:


desc_3=driver.find_element_by_xpath("//div[@class='clearboth description']")
z=desc_3.text.replace('\n','')
z


# In[91]:


c=z.split('\n')
c


# In[21]:


U_4='https://www.naukri.com/job-listings-specialist-i-data-scientist-philips-india-limited-bangalore-bengaluru-4-to-7-years-170521500993?src=jobsearchDesk&sid=16217377231564440&xp=4&px=1'


# In[93]:


driver.get(U_4)


# In[95]:


desc_4=driver.find_element_by_xpath("//section[@class='job-desc']")
z_1=desc_4.text.replace('\n','')
z_1


# In[97]:


d=z_1.split('\n')
d


# In[99]:


U_5='https://www.naukri.com/job-listings-data-scientist-ibm-india-pvt-limited-bangalore-bengaluru-6-to-8-years-110521907352?src=jobsearchDesk&sid=16217378987369811&xp=5&px=1'


# In[100]:


driver.get(U_5)


# In[103]:


desc_5=driver.find_element_by_xpath("//div[@class='nConfig_textblock ']")
z_2=desc_5.text.replace('\n','')
z_2


# In[105]:


e=z_2.split('\n')
e


# In[106]:


#oracle
U_6=("https://www.naukri.com/job-listings-data-scientist-oracle-india-pvt-ltd-bangalore-bengaluru-6-to-10-years-190521008276?src=jobsearchDesk&sid=16217381035251411&xp=5&px=1")


# In[109]:


driver.get(U_6)


# In[111]:


dec_6=driver.find_element_by_xpath("//section[@class='getJobDescriptionOtherDetails JD av_textblock_section jDisc mt25']")
z_3=dec_6.text.replace('\n','')
z_3


# In[113]:


f=z_3.split('\n')
f


# In[114]:


#SDE
U_7=("https://www.naukri.com/job-listings-sde-lead-data-scientist-l3-huawei-technologies-india-pvt-ltd-bangalore-bengaluru-5-to-8-years-120521901434?src=jobsearchDesk&sid=16217384726649702&xp=7&px=1")


# In[115]:


driver.get(U_7)


# In[117]:


dec_7=driver.find_element_by_xpath("//div[@class='dang-inner-html']")
z_4=dec_7.text.replace('\n','')
z_4


# In[119]:


g=z_4.split('\n')
g


# In[120]:


U_8=("https://www.naukri.com/job-listings-computational-design-lead-data-scientist-l3-huawei-technologies-india-pvt-ltd-bangalore-bengaluru-5-to-8-years-120521901329?src=jobsearchDesk&sid=16217398441625711&xp=8&px=1")


# In[121]:


driver.get(U_8)


# In[126]:


desc_8=driver.find_element_by_xpath("//div[@class='dang-inner-html']")
z_5=desc_8.text.replace('\n','')
z_5


# In[127]:


h=z_5.split('\n')
h


# In[129]:


U_9=("https://www.naukri.com/job-listings-hiring-for-data-scientist-on-contract-basis-3-6-months-globaledx-learning-and-technology-solution-pvt-ltd-hyderabad-secunderabad-bangalore-bengaluru-mumbai-all-areas-3-to-8-years-170521003581?src=jobsearchDesk&sid=16217400843896727&xp=9&px=1")


# In[130]:


driver.get(U_9)


# In[132]:


#globaledx
desc_9=driver.find_element_by_xpath("//section[@class='job-desc']")
z_6=desc_9.text.replace('\n','')
z_6


# In[133]:


i=z_6.split('\n')
i


# In[134]:


U_10=("https://www.naukri.com/job-listings-software-engineer-ios-customer-platforms-go-jek-india-bangalore-bengaluru-2-to-7-years-210521500781?src=jobsearchDesk&sid=16217403057212721&xp=1&px=1")


# In[135]:


driver.get(U_10)


# In[137]:


desc_10=driver.find_element_by_xpath("//div[@class='dang-inner-html']")
z_7=desc_10.text.replace('\n','')
z_7


# In[140]:


j=z_7.split('\n')
j


# In[142]:


Full_Job_Description=a+b+c+d+e+f+g+h+i+j
Full_Job_Description


# In[147]:


df=pd.DataFrame({})
df['job-title']=Title[0:10]
df['job-location']=Lcation[0:10]
df['company_name']=Company [0:10]
df['full job-description']=Full_Job_Description
df


# In[ ]:




