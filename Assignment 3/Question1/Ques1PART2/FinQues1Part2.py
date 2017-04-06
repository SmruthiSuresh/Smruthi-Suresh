
# coding: utf-8

# ## Question 1 Part 2

# In[4]:

#importing all the required libraries
import pandas as pd
import csv
import datetime

df1=pd.read_csv('vehicle_collisions.csv')
df1.head()


# In[25]:

groupedByBorough=pd.DataFrame(df1.groupby(['BOROUGH']).size().reset_index())
groupedByBorough


# In[26]:

groupedByBorough['One Vehicle Involved']=groupedByBorough['BOROUGH'].apply(lambda x: len(df1[(df1['BOROUGH']==x)
& (df1['VEHICLE 1 TYPE'].isnull()==False)& (df1['VEHICLE 2 TYPE'].isnull()==True) & (df1['VEHICLE 3 TYPE'].isnull()==True)
& (df1['VEHICLE 4 TYPE'].isnull()==True)& (df1['VEHICLE 5 TYPE'].isnull()==True)]))
                 
                 
                


# In[27]:

groupedByBorough['Two Vehicles Involved']=groupedByBorough['BOROUGH'].apply(lambda x: len(df1[(df1['BOROUGH']==x)
& (df1['VEHICLE 1 TYPE'].isnull()==False) & (df1['VEHICLE 2 TYPE'].isnull()==True) & (df1['VEHICLE 3 TYPE'].isnull()==True)
 & (df1['VEHICLE 4 TYPE'].isnull()==True)   & (df1['VEHICLE 5 TYPE'].isnull()==True)]))               
                 
                 
                


# In[28]:

groupedByBorough['Three Vehicles Involved']=groupedByBorough['BOROUGH'].apply(lambda x: len(df1[(df1['BOROUGH']==x)
& (df1['VEHICLE 1 TYPE'].isnull()==False) & (df1['VEHICLE 2 TYPE'].isnull()==True) & (df1['VEHICLE 3 TYPE'].isnull()==True)
 & (df1['VEHICLE 4 TYPE'].isnull()==True)   & (df1['VEHICLE 5 TYPE'].isnull()==True)])) 


# In[29]:

groupedByBorough['Four Vehicles Involved']=groupedByBorough['BOROUGH'].apply(lambda x: len(df1[(df1['BOROUGH']==x)
& (df1['VEHICLE 1 TYPE'].isnull()==False) & (df1['VEHICLE 2 TYPE'].isnull()==True) & (df1['VEHICLE 3 TYPE'].isnull()==True)
 & (df1['VEHICLE 4 TYPE'].isnull()==True)   & (df1['VEHICLE 5 TYPE'].isnull()==True)])) 


# In[30]:

groupedByBorough['Five Vehicles Involved']=groupedByBorough['BOROUGH'].apply(lambda x: len(df1[(df1['BOROUGH']==x)
& (df1['VEHICLE 1 TYPE'].isnull()==False) & (df1['VEHICLE 2 TYPE'].isnull()==True) & (df1['VEHICLE 3 TYPE'].isnull()==True)
 & (df1['VEHICLE 4 TYPE'].isnull()==True)   & (df1['VEHICLE 5 TYPE'].isnull()==True)])) 


# In[31]:

groupedByBorough


# In[33]:


groupedByBorough.to_csv(r'C:\Users\smrut\Documents\Python\PythonAssignment3\Assignment 3\Ques1Part2Result.csv', sep=',')

