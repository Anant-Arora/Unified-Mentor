#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as num
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data= pd.read_csv("Amazon Sales data.csv")


# In[3]:


data


# In[4]:


data.info()


# In[5]:


data.describe()


# In[6]:


data.head()


# # Most Profitable Region

# In[11]:


most_profit= data.sort_values(by="Total Profit", ascending= False)


# In[12]:


most_profit


# # Total Profit 

# In[18]:


Total_profit= data.groupby("Item Type")['Total Profit'].sum()


# In[19]:


Total_profit.sort_values(ascending= False)


# In[30]:


Total_revenue= data.sort_values(by="Total Revenue", ascending= False)


# In[34]:


Total_revenue.head(10)


# Most Revenue Was made in Central America and the Caribbean about 5997054.98

# # Offline Vs Online

# In[65]:


Sales_channel= data.groupby("Sales Channel")["Units Sold"].sum().reset_index()


# In[66]:


sns.barplot(data=Sales_channel, x="Sales Channel", y='Units Sold')
plt.title("Units Sold by Way Of Selling")
plt.show()


# In[46]:


Sales_channel


# Offline Chanels sells more unit of goods then online.

# In[49]:


region_sales = data.groupby('Region')['Total Revenue'].sum().reset_index()
plt.xticks(rotation=30)
sns.barplot(data=region_sales, x='Region', y='Total Revenue')
plt.title('Sales by Region')
plt.show()


# We can see from the graph that most revenue generated was by Central America and the Carebean

# # Sales By Item Type

# In[51]:


item_sales = data.groupby('Item Type')['Total Revenue'].sum().reset_index()
plt.xticks(rotation=30)
sns.barplot(data=item_sales, x='Item Type', y='Total Revenue')
plt.title('Sales by Item Type')
plt.show()


# Cosmetics was sold the most which generated about 3.5 thousand crores of revenue.

# # Average Sales And Profit per order

# In[54]:


average_sales_per_order = data['Total Revenue'].mean()
print(f'Average Sales per Order: {average_sales_per_order}')


# In[59]:


average_profit_per_order = data['Total Profit'].mean()
print(f'Average Profit per Order: {average_profit_per_order}')


# # Year Wise Sales Trend

# In[67]:


data['Order Date']= pd.to_datetime(data['Order Date'])


# In[70]:


data['Order Year'] = data['Order Date'].dt.year


# In[72]:


year_sales = data.groupby('Order Year')['Total Revenue'].sum().reset_index()
sns.lineplot(data=year_sales, x='Order Year', y='Total Revenue')
plt.title('Year-wise Sales Trend')
plt.show()


# In[73]:


sns.scatterplot(x="Total Revenue", y="Total Profit", data=data)
plt.show()


# we can conclude that there is positive relation between Profit and Revenue.
