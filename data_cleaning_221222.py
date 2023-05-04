#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import ipaddress
import re
import numpy as np


# In[ ]:


PT1 = pd.read_csv('/Users/danielchiang/Dropbox/PTT_data/arti_data_700_932.csv', sep=",", header = None)
PT2 = pd.read_csv('/Users/danielchiang/Dropbox/PTT_data/arti_data_932_4549.csv', sep=",", header = None)
PT3 = pd.read_csv('/Users/danielchiang/Dropbox/PTT_data/arti_data.csv', sep=",", header = None, on_bad_lines='warn')


# In[ ]:


PT1 = pd.concat([PT1[0].str.split(' ',1 ,expand=True), PT1[2].str.split(']',1 ,expand=True), PT1[3].str.split(' ',expand=True), PT1[4], PT1[5]], axis=1)
PT2 = pd.concat([PT2[0].str.split(' ',1 ,expand=True), PT2[2].str.split(']',1 ,expand=True), PT2[3].str.split(' ',expand=True), PT2[4], PT2[5]], axis=1)
PT3 = pd.concat([PT3[0].str.split(' ',1 ,expand=True), PT3[2].str.split(']',1 ,expand=True), PT3[3].str.split(' ',expand=True), PT3[4], PT3[5]], axis=1)


# In[ ]:


PT1.columns = ['user_ID', 'user_name', 'post_type', 'post_title', 'day', 'month', 'date', 'time', 'year', 'IP_address', 'article']
PT2.columns = ['user_ID', 'user_name', 'post_type', 'post_title', 'day', 'month', 'date', 'time', 'year', 'check', 'IP_address', 'article']
PT3.columns = ['user_ID', 'user_name', 'post_type', 'post_title', 'day', 'month', 'date', 'time', 'year', 'check', 'IP_address', 'article']

Article = pd.concat([PT2,PT3],axis=0,ignore_index=True)


# In[ ]:


ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
PT1 = PT1[PT1['IP_address'].str.match(ip_pattern, na=False)]
PT1['IP_address'] = PT1['IP_address'].apply(lambda x: int(ipaddress.ip_address(x)))

Article = Article[Article['IP_address'].str.match(ip_pattern, na=False)]
Article['IP_address'] = Article['IP_address'].apply(lambda x: int(ipaddress.ip_address(x)))


# In[ ]:


Article['date'] = pd.to_numeric(Article['date'],errors = 'coerce')
Article.loc[Article.date.isnull(), 'date'] =  Article.loc[Article.date.isnull(), 'time']
Article.loc[Article.date == Article.time, 'time'] =  Article.loc[Article.date == Article.time, 'year']
Article.loc[Article.time == Article.year, 'year'] =  Article.loc[Article.time == Article.year, 'check']

Article = pd.concat([PT1,Article],axis=0,ignore_index=True)
Article = Article.drop(columns=['check','article'])


# In[ ]:


Article = Article.dropna().astype({'date':'int'})


# In[ ]:


Article.to_csv('article.csv',index = 0, header = 0, line_terminator = '\n')


# In[ ]:





# In[ ]:





# In[ ]:





# In[74]:


PT1_pu = pd.read_csv('push_data_700_932.csv', sep=",", header = None)
PT2_pu = pd.read_csv('push_data_932_4549.csv', sep=",", header = None)
PT3_pu = pd.read_csv('push_data.csv', sep=",", header = None, on_bad_lines='warn')


# In[80]:


ip_pattern_p = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
date_pattern_p = re.compile(r'((0?[1-9]|1?[0-2])/(0[1-9]|[12]?[0-9]|3?[01]))')
time_pattern_p = re.compile(r'(2?[0-3]|[0-1]?[0-9]):([0-5]?[0-9])')


# In[76]:


Comments = pd.concat([PT1_pu,PT2_pu,PT3_pu],axis=0,ignore_index=True)


# In[81]:


Comments[6].str.extract(ip_pattern_p)
Comments[6].apply(lambda x: re.match(ip_pattern_p,x).group(0)))


# In[ ]:


Comments = pd.concat([Comments[0].str.split(' ',1 ,expand=True), Comments[2].str.split(']',1 ,expand=True), Comments[3], Comments[4], IP, axis=1)


# In[91]:


IP = Comments[6].apply(lambda x: re.match(ip_pattern_p,x).group(0) if re.search(ip_pattern_p,x) else np.nan)


# In[ ]:





# In[87]:





# In[92]:


Comments


# In[ ]:


a


# In[19]:





# In[10]:





# In[24]:


print(re.match(r'\d',Comments[6][0]))


# In[89]:


print(type(re.match(ip_pattern_p,Comments[6][9587120])))


# In[73]:


Comments[6].str.findall(date_pattern_p)


# In[72]:


def test(z):
    


# In[ ]:


Comments[6].str.contains()


# In[ ]:





# In[ ]:




