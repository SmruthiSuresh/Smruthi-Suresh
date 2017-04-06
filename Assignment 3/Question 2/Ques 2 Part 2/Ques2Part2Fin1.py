
# coding: utf-8

# # Question 2 Part 2

# In[1]:

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[2]:

# Reading the csv File
dfa=pd.read_csv('employee_compensation.csv')
dfa.head()


# In[8]:

# Filtering by the year type Calendar
dfb=dfa[dfa['Year Type']=='Calendar']
dfb.head()


# In[11]:

#Calculating the Mean by grouping the Dataframe based on Job Family and Employee Identifier
dfc=dfb.groupby(['Job Family','Employee Identifier']).mean().reset_index()
dfc.head()


# In[13]:

#Calculating percentage of overtime first
dfc['Overtime']=(dfc.Overtime/dfc.Salaries)*100
dfc


# In[16]:

#Checking whether the money earned in overtime is greater than 5 percent of the salary
dfd=dfc[dfc.Overtime > 5]
dfd


# In[19]:

#Finding mean Total Benefits and Total Compensation based on the Job Family
dfe=dfd.groupby('Job Family')['Total Benefits','Total Compensation'].mean().reset_index()
dfe.head()


# In[23]:

#calculating percent Total Benefits
dfe['Percent_Total_Benefit']=(dfe['Total Benefits']/dfe['Total Compensation'])*100
dfe


# In[26]:

result=dfe.sort('Percent_Total_Benefit',ascending=False).reset_index()
result


# In[27]:

#Writing the output to a csv file
result.to_csv('Q2Part2Result.csv', sep=',')

