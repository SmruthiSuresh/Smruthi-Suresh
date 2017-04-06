
# coding: utf-8

# # Question 3 Part 1

# In[3]:

import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[35]:

# Read te csv file
dfa=pd.read_csv('cricket_matches.csv')
dfa.head()


# In[13]:

#Filtering the frame with both home and the winner being the same
dfa=dfa[dfa.home == dfa.winner]
dfa


# In[17]:

dfb=dfa[dfa.home==dfa.winner]


# In[19]:

# Scores is calculated by giving a condition that if the innings1 ans the winner are same then runs of innings1
#has to be taken else the runs of innings2
dfb["Scores"] = np.where((dfb['innings1']==dfb['winner']), dfb['innings1_runs'], dfb['innings2_runs'])
dfb.head()


# In[33]:

# Average score are calculated based on the home
Average_Score=dfb.groupby('home').Scores.mean()
dfc=pd.DataFrame(Average_Score)
dfc


# In[34]:

#Output is written to a csv file
dfc.to_csv('Q3Part1Result.csv', sep=',')


# In[87]:



    


# In[ ]:



