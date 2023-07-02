#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import seaborn as sns


# In[2]:


fl = pd.read_csv('E:Stanford Open Policing Project-FL/FL.csv')


# In[3]:


fl.head(92)


# ### Exploratory

# In[4]:


fl.info()


# In[5]:


num_null = fl.isnull().sum()
num_null


# In[6]:


fl.shape


# In[7]:


fl.columns


# In[8]:


#percentage of null values
perct = (num_null / fl.shape[0]) * 100
perct


# ### Reduce not needed columns

# In[9]:


#drop columns with missing data greater than 25% or has duplicate data
fl = fl.drop(columns = ['fine_grained_location', 'police_department', 'driver_age_raw', 'driver_race_raw', 'violation_raw', 'search_type', 'state', 'county_name', 'county_fips'])


# In[10]:


#diplay of columns now in dataframe
fl.columns


# In[11]:


(fl.isnull().sum()/fl.shape[0])*100


# ### Stop date 

# In[12]:


fl.stop_date.describe()


# In[13]:


fl.stop_date.info()


# In[14]:


fl.stop_date.min()


# In[15]:


fl.stop_date.max()


# In[16]:


print(fl.stop_date)


# ### Driver age

# In[17]:


fl.driver_age.describe().round()


# In[18]:


#distribution driver age
plt.hist(fl['driver_age'], bins=10, facecolor = 'b')
plt.xlabel('driver_age')
plt.ylabel('Count')
plt.title('Distribution of Driver\'s Age')
plt.show()


# In[19]:


# number of NA values in driver_age
fl.driver_age.isna().sum()


# In[20]:


fl.driver_age.value_counts()


# ### driver age has a high amount of null values 1128897, filling values with the mean creates an unusually high concentration of persons of that age, which would skew any analysis following
# 
# #### As such we will eliminate all null values for the dataframe fl

# ### Eliminate rows with Null Values

# In[21]:


#drop all rows with NaN values
fl.dropna(axis=0, inplace=True)


# In[22]:


#no null values in dataframe
fl.isnull().sum().round()


# #### Returning to driver_age, for analysis

# In[23]:


fl.driver_age.isnull().sum()


# In[24]:


#distribution driver age
plt.hist(fl['driver_age'], bins=10, facecolor = 'b')
plt.xlabel('driver_age')
plt.ylabel('Count')
plt.title('Distribution of Driver\'s Age')
plt.show()


# In[25]:


#reduced number of rows by droping na rows in fl
fl.driver_age.describe().round()


# In[26]:


fl.shape


# In[27]:


fl.columns


# ### Location of stops

# In[28]:


# location raw value counts
fl.location_raw.value_counts()


# In[29]:



plt.hist(fl['location_raw'], bins=50, rwidth = .7, facecolor = 'g')
plt.xlabel('location')
plt.ylabel('Count')
plt.xticks(rotation = 90)
plt.title('Distribution of Location')
plt.show()


# ### Officers Gender

# In[30]:


# dataframe officer gender counts
gender = pd.DataFrame(fl.officer_gender.value_counts())
gender 


# In[31]:


# male officer gender
ofcM = (fl['officer_gender'] == 'M').sum()
ofcM


# In[32]:


# female officer gender
ofcF = (fl['officer_gender'] == 'F').sum()
ofcF


# In[33]:


# difference in officer genders
gender_diff = ofcM - ofcF
gender_diff


# In[34]:


# barplot of officer gender
gender.plot.bar(figsize = (15, 10))
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Count of Gender')
plt.show()


#  ### Officer Age

# In[35]:


round(fl.officer_age.describe())


# In[36]:


fl.officer_age.min()


# In[37]:


fl.officer_age.max()


# In[38]:


#ages below 18 are errors as must be at least 18 to be officer, and officers over 70 appear to outliers, these will be removed
fl = fl[fl['officer_age'] < 70]
fl = fl[fl['officer_age'] > 17]


# In[39]:


#dataframe now reflects more accurate description of officer ages
fl.officer_age.describe().round()


# In[40]:


# histogram of officers ages
plt.hist(fl['officer_age'], bins=10, facecolor = 'b')
plt.xlabel('officer_age')
plt.ylabel('Count')
plt.title('Distribution of Officer\'s Age')
plt.show()


# In[41]:


fl['officer_age'].isnull().sum()


# In[42]:


#Officers ages
age = pd.DataFrame(fl.officer_age.value_counts())
age


# In[43]:


#bar plot of officers ages
age.plot.bar(figsize = (15, 10))
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Officer Age')
plt.show()


# ### Officer Rank

# In[44]:


# making all column variations of Trooper the same TPR
fl['officer_rank'] = fl['officer_rank'].replace(["TROOPER", "TPR.", "TPOOPER", "S-TROOPER"], "TPR") 


# In[45]:


# changing column variations of sergeant, lt., sr. Trooper and corporal to abreviations of 
fl['officer_rank'] = fl['officer_rank'].replace(["SERGEANT", "LT.", "SR.TROOPER", "CORPORAL"], ["SGT", "LT", "SR TPR", "CPL"])


# In[46]:


# making all column names of to abreviations
fl['officer_rank'] = fl['officer_rank'].replace(["LIEUTENANT", "OFFICER", "SERGEANT`", "SR TROOPER"], ["LT", "OFC", "SGT", "SR TPR"]) 


# In[47]:


# checking for abreviations
fl['officer_rank']


# In[48]:


# checking column variables counts
rank = pd.DataFrame(fl.officer_rank.value_counts())
rank 


# In[50]:


# bar plot of officer ranks
rank.plot.bar(figsize = (15, 10))
plt.xlabel('rank')
plt.ylabel('Count')
plt.title('Count of Officer Rank')
plt.show()


# ### Officer Race

# In[51]:


# officer race counts
race = fl.officer_race.value_counts()
race


# In[52]:


# bar plot of race counts
race.plot.bar(figsize = (15, 10))
plt.xlabel('race')
plt.ylabel('Count')
plt.title('Count of Officer Race')
plt.show()


# In[53]:


# pie chart of percentage of officer race
labels='White', 'Black', 'Hispanic', 'Other', 'Asian'
race.plot(kind='pie', figsize=(4,4), title='Percentage of Race', labels=labels, label='', explode=(0.1, 0.1, 0.1, 0.1, 0.1), autopct='%1.1f%%')


# ### Stop outcome

# In[54]:


# stop outcome variable counts
outcome = fl.stop_outcome.value_counts()
outcome


# In[55]:


# pie chart of percentages of stop outcomes
labels='Citation', 'Warning', 'Misdemeanor Arrest', 'Faulty Equipment Notice', 'Felony Arrest'
outcome.plot(kind='pie', figsize=(4,4), title='Percentage of Stop Outcomes', labels=labels, label='', explode=(0.1, 0.1, 0.1, 0.1, 0.1), autopct='%1.1f%%')


# In[56]:


#percentage of stop outcomes, rounded
pctoutcome = round((fl.stop_outcome.value_counts()/fl.shape[0])*100)
pctoutcome


# In[ ]:




