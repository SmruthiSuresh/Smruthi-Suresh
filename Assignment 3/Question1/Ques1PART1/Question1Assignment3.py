
# coding: utf-8

# # Question 1 Part 1

# In[193]:

# Importing necessary Libraries
import pandas as pd
import csv
import datetime
from datetime import datetime as dt



# In[198]:

#Reading the csv file
df=pd.read_csv('vehicle_collisions.csv',parse_dates=['DATE'])
df.head()


# In[ ]:




# In[199]:

# Filtering by the year 2016 and Borough Manhattan
dfi = df.loc[(df['DATE'] > '1/1/2016') & (df['DATE'] <= '12/31/2016') & (df['BOROUGH']=='MANHATTAN')]


# In[201]:

# Extracting the month from the date column
dfi['Month']=dfi['DATE'].dt.strftime('%B')
dfi.head()


# In[203]:

#Counting the collisions month-wise in NYC.
dm=dfi.groupby('Month').BOROUGH.agg(['count'])


# In[205]:

#Displaying the Data Frame
#dm.append(df.BOROUGH)
dm.head()


# In[134]:

df=df.rename(columns = {'UNIQUE KEY':'UNIQUE_KEY'})
df.head()


# In[163]:


counts_df = pd.DataFrame(df.groupby('Month').size().rename('TotalNoOfAccidentsInNyc'))
counts_df.head()


# In[167]:

dm['TotalAccidentsInNYC']= counts_df['TotalNoOfAccidentsInNyc']
dm.head()


# In[174]:

#Calculating percentage accidents in manhattan to the total number of accidents in Newyork
dm['PERCENTAGE'] = (dm['count'] / dm['TotalAccidentsInNYC']) *100
dm.head()


# In[195]:

dm=dm.rename(columns = {'count':'MANHATTAN'})
dm.head()

#dm.to_csv(file_name, sep='\t', encoding='utf-8')


# In[197]:

#Writing the output to a csv file
dm.to_csv('Q1Part1Result.csv', sep=',')


# In[191]:






# In[ ]:






# In[ ]:




# In[ ]:




# In[186]:




# In[188]:




# In[182]:




# In[ ]:




# In[184]:



