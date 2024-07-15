#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as num
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


data= pd.read_excel("Bird Data set new.xlsx")


# In[23]:


data


# In[24]:


new_data= data.drop("Is Aircraft Large?", axis=1)


# In[25]:


new_data= data.drop("Wildlife: Size", axis=1)


# In[26]:


new_data= data.drop("Number of people injured", axis=1)


# In[27]:


new_data= data.drop("Is Aircraft Large?", axis=1)


# In[28]:


new_data= data.drop("Aircraft: Make/Model", axis=1)


# In[29]:


new_data= data.drop("Aircraft: Type", axis=1)


# In[30]:


new_data


# In[11]:


new_data.describe()


# 1. Total number of peoples injured by the bird strike= 25558
# 2. Most of the Aircrafts were flying at an height of 800 Feet above the ground
# 3. Max number of people injured= 6

# In[12]:


new_data.info()


# In[13]:


new_data= new_data.sort_values(by="Wildlife: Number Struck Actual", ascending= False)


# # Top 10 US Airlines with most bird hits are as follows:

# In[14]:


new_data.head(10)


# # Top 50 Airports with most bird strike are as follows:

# In[36]:


new_data.head(50)


# In[57]:


sns.scatterplot(x='Wildlife: Number Struck Actual', y='Feet above ground', data=data)


# In[37]:


Total_cost= new_data.groupby("Year")['Cost: Total $'].sum()


# In[61]:


plt.bar(new_data['Wildlife: Number Struck Actual'], new_data['Feet above ground'])
plt.xlabel("wildlife strikes")
plt.ylabel("Feet Above Ground")
plt.title("Bird Strikes")
plt.show()


# Most number of Bird stike happens at 1000 Feet above the ground with approx 230 strikes.
# At 12500 Feet above the ground also 100 Bird strikes.

# # Effect Of Bird Strike

# In[64]:


effect_of_strike = new_data['Effect: Impact to flight'].value_counts()

plt.figure(figsize=(12, 6))
effect_of_strike.plot(kind='bar', color='brown')
plt.title('Effect of Bird Strikes on Flight')
plt.xlabel('Effect')
plt.ylabel('Number of Strikes')
plt.xticks(rotation=45)
plt.show()


# From the above data we can see that Majority of Bird Strikes were caused noting to the aircraft body.
# 
# 1500 Bird Strikes caused Precautionary Landing.
# 
# About 1000 bird strike led to aborted Take Off

# # Were Pilots Informed? & Prior Warning and Effect of Strike Relation
# 

# In[66]:


pilots_informed = new_data['Pilot warned of birds or wildlife?'].value_counts()

plt.figure(figsize=(12, 6))
pilots_informed.plot(kind='bar', color='grey')
plt.title('Were Pilots Informed Prior to Bird Strikes?')
plt.xlabel('Pilots Informed')
plt.xticks(rotation=0)
plt.show()


# Around 14000 Pilots were not informed about the bird stike and 11000 Pilots were unformed about the bird strike

# In[67]:


prior_warning_effect = new_data.groupby(["Pilot warned of birds or wildlife?", 'Effect: Indicated Damage']).size().unstack(fill_value=0)

prior_warning_effect.plot(kind='bar', stacked=True, figsize=(12, 6), color=['green', 'orange', 'red', 'black'])

plt.title("Effect Vs Damage relation")
plt.xlabel('Pilots Informed')
plt.ylabel('Number of Strikes')
plt.show()


# After seeing the visualization we can conclude that 2000 times the aircraft was damaged when the pilot was not informed and 14000 aircrafts were not damaged.
# 1000 aircrafts recieved damage even after the pilots came to know about the bird strike.
# we can conclude that the pilots which recieved the information about the bird strike saved the aircraft with no damage.

# # Effect of Strike at Different Altitude
# 

# In[73]:


new_data


# In[75]:


plt.figure(figsize=(12, 6))
plt.bar(new_data['Effect: Indicated Damage'], new_data['Feet above ground'])
plt.xlabel("Strike Effect")
plt.ylabel("Feet Above")
plt.title("Effect At different altitude")
plt.show()


# # Altitude of aeroplanes at the time of strike

# In[81]:


plt.figure(figsize=(12, 6))
Strike_Altitude = new_data.groupby('Altitude bin')['Wildlife: Number Struck Actual'].mean()
Strike_Altitude.plot(kind='bar', color='skyblue')
plt.xlabel("Altitude bin")
plt.ylabel("Wildlife: Number Struck Actual")
plt.title("Alltitude at the time of hit")
plt.show()


# we can conclude that the number of Bird Strike was much higher when the flight was nuder 1000 Feet of altitude. It is double that of the planes more than 1000 Feet

# # Average Altitude of the aeroplanes in different phases at the time of strike
# 

# In[84]:


Average_altitude= new_data.groupby('When: Phase of flight')['Feet above ground'].mean()
plt.figure(figsize=(12, 6))
Average_altitude.plot(kind='bar', color='magenta')
plt.title('Average Altitude of Airplanes in Different Phases at the Time of Strike')
plt.xlabel('Phase of Flight')
plt.ylabel('Average Altitude (feet)')
plt.xticks(rotation=45)
plt.show()


# We can clearly interpret that the around 6000 bird strike happened while the plan was descending.
# 1200 when the plane was about to fly.
# 1000 when the plane approached the airport

# In[ ]:




