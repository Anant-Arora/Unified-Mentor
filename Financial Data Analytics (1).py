#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


data= pd.read_csv("Financial Analytics data.csv")


# In[13]:


data


# In[14]:


data.head()


# In[41]:


data.info()


# In[40]:


data.describe()


# 1.Max number of companies= 500
# 
# 2.Mean of Market Cap= 28043.85 crores
# 
# 3.Max Market Cap= 583436.720000 crores
# 
# 4.Minimum Market Cap of a company= 3017 crores
# 
# 5.Mean of Sales= 4395.976849 crores
# 
# 6.Max Sales= 110666.930000 crores
# 
# 7.Minimum Sales= 47.240000 crores

# In[22]:


sns.scatterplot(x='Mar Cap - Crore',y='Sales Qtr - Crore', data=data)
plt.title("capitalization Vs Sales")
plt.xlabel("Market Capitalization (crores)")
plt.ylabel("Sales (Crores)")
plt.show()


# The scatter plot shows that small companies are more common in India because of the dense dots present in the left hand side of the graph. Majority of comany are valued under 100000 crores whose sales come under 20000 crores. Very few points are outside the pattern for instance compnay whose sales are more than 100000 crores. This means some company are undervalued.

# In[43]:


sns.displot(data['Mar Cap - Crore'])
plt.title("Distribution of Capitalization")
plt.xlabel("Market Cap (crore)")
plt.show()


sns.displot(data["Sales Qtr - Crore"])
plt.title("Distribution of Sales")
plt.xlabel("Sales (crore)")
plt.show()


# The given two graphs clearly display a positive trend between Sales and Market Capitalisation. There is positive trend in the market which means that the company with higher valuation has more sales as compared to the company with small valuation. Number of company wiht higer sales are very low as the tale of the graph is long that display few number of big companies and more small cap company are present in the market.
