#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\ralia\Desktop\Work\country_vaccination_stats.csv")


# In[6]:


df.head()


# In[12]:


df.isnull().sum()


# In[15]:


df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)


# In[16]:


df.isnull().sum()

