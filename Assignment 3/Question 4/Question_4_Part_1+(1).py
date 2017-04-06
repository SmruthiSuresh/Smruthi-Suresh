
# coding: utf-8

# #### 

# In[1]:

# Importing all the libraries
import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[5]:

# Reading the csv file
dfa=pd.read_csv(r'movies_awards.csv')


# In[6]:

#Extracting The number of awards seperately for wins and nominations
dfa['Awards_Won'] = dfa['Awards'].str.extract('(\d+) win', expand=True)
dfa['Awards_Nominated'] = dfa['Awards'].str.extract('(\d+) nomination', expand=True)
dfa['PrimeAwards_Won']= dfa['Awards'].str.extract('Won (\d+) Primetime', expand=True)
dfa['PrimeAwards_Nominations']= dfa['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
dfa['BaftaAwards_Won']= dfa['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
dfa['BaftaAwards_Nominations']= df['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
dfa['OscarAwards_Won']= dfa['Awards'].str.extract('Won (\d+) Oscar', expand=True)
dfa['OscarAwards_Nominations']= dfa['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
dfa['GoldenGlobeAwards_Won']= dfa['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
dfa['GoldenGlobeAwards_Nominations']= dfa['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)


# In[9]:

#Displaying only the necessary output columns

dfb = dfa[dfa.columns[15:30]]
dfcOutput = dfb.fillna(0)


# In[6]:




# In[10]:

dfcOutput


# In[11]:

#converting the types of the pandas objects to numeric ie int
dfcOutput['Awards_Won'] = dfcOutput['Awards_Won'].astype(str).astype(int)
dfcOutput['PrimeAwards_Won'] = dfcOutput['PrimeAwards_Won'].astype(str).astype(int)
dfcOutput['BaftaAwards_Won']=dfcOutput['BaftaAwards_Won'].astype(str).astype(int) 
dfcOutput['OscarAwards_Won']=dfcOutput['OscarAwards_Won'].astype(str).astype(int) 
dfcOutput['GoldenGlobeAwards_Won']=dfcOutput['GoldenGlobeAwards_Won'].astype(str).astype(int)


# In[14]:

dfcOutput['Awards_Nominated'] =dfcOutput['Awards_Nominated'].astype(str).astype(int) 
dfcOutput['PrimeAwards_Nominations']=dfcOutput['PrimeAwards_Nominations'].astype(str).astype(int)
dfcOutput['BaftaAwards_Nominations']=dfcOutput['BaftaAwards_Nominations'].astype(str).astype(int)
dfcOutput['OscarAwards_Nominations']=dfcOutput['OscarAwards_Nominations'].astype(str).astype(int)  
#dfcOutput['GoldenGlobeAwards_Nominations']=dfcOutput['GoldenGlobeAwards_Nominations'].astype(str).astype(int)


# In[17]:

#Totalling up the awards won by each movie
dfcOutput['Awards Won Or Nominated'] = dfcOutput['Awards_Won']+dfcOutput['Awards_Nominated']


# In[17]:




# In[18]:

#Displaying Output
dfcOutput.head()


# In[21]:

#Writing output to csv file
dfcOutput.to_csv('Ques4Part1Result.csv')

