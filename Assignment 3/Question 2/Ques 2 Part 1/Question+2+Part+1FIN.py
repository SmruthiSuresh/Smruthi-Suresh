
# coding: utf-8

# # Ques2 Part 1

# In[21]:

#importing all the required libraries
import pandas as pd
import csv
import datetime
df4=pd.read_csv('employee_compensation.csv')
df4.head()


# In[22]:

#Reading the csv file and displaying first 5 columns
df5=df4.rename(columns = {'Total Compensation':'Total_Compensation','Organization Group':'Organization_Group'})

df5.head()


# In[23]:

#Finding the Average of Total Compensation by grouping based on Department and Organization Group
df6=pd.DataFrame(df5.groupby(['Organization_Group','Department'],sort=True).Total_Compensation.mean())
df6


# In[20]:

#Writing the output to a csv file
df6.to_csv('Q2Part1Result.csv', sep=',')

