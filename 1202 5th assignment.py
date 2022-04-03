#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


#Read csv file
df_youtube= pd.read_csv("top_1000_youtubers.csv",sep=",", encoding='ISO-8859-1')
print("done")


# In[7]:


df_youtube.head(10)


# In[8]:


# Top 1000 Youtube Channel with most no. of Sucscribers
top_1000_youtubers=df_youtube.head(1000)


# In[9]:


#Show graphs withint Python notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


# Use regular matplotlib function to display a barplot of distribution of channels
top_1000_youtubers.groupby(['channeltype'])['userID'].count().plot(kind='bar')


# In[ ]:




