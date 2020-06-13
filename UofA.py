#!/usr/bin/env python
# coding: utf-8

# **Import the csv file into the data fram using pandas function read_csv

# In[1]:




import pandas as pd

df= pd.read_csv(r'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

df


# **Select only those states where value is Arizona using df.loc function

# In[4]:


df=df.loc[df['state'] == 'Arizona']


# **convert the file to excel using to_excel function, add the file path followed by filename

# In[15]:


df.to_excel(r'C:\Users\pawan\Desktop\PYTHON\Covid_arizona.xlsx', index = False)

