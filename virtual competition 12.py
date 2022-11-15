#!/usr/bin/env python
# coding: utf-8

# Consider the following Python dictionary `data` and Python list `labels`:
# 
# ``` python
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# ```
# 
# **1.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# In[3]:


df=pd.DataFrame(data,index=labels)
print(df)


# **2.** Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

# In[7]:


print(df.info())


# **3.** Return the first 3 rows of the DataFrame `df`.

# In[8]:


df.head(3)


# **4.** Display the 'animal' and 'age' columns from the DataFrame `df`

# In[9]:


df[['animal','age']]


# **5.** Display the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']'

# In[13]:


print(df.iloc[[3,4,8],[0,1]])


# **6.** Select only the rows where the number of visits is greater than 3.

# In[14]:


print(df[df['visits']>3])


# **7.** Select the rows where the age is missing, i.e. it is `NaN`.

# In[18]:


print(df[df['age'].isnull()])


# **8.** Select the rows where the animal is a cat *and* the age is less than 3.

# In[29]:


print(df.loc[(df['animal']=='cat')&(df['age']<3)])


# **9.** Select the rows where the age is between 2 and 4 (inclusive)

# In[34]:


print(df.loc[(df['age']>=2)&(df['age']<=4)])


# **10.** Change the age in row 'f' to 1.5.

# In[41]:


df.loc['f','age']=1.5
print(df)


# **11.** Calculate the sum of all visits in `df` (i.e. the total number of visits).

# In[42]:


sum(df['visits'])


# **12.** Calculate the mean age for each different animal in `df`.

# In[47]:


df['age'].mean()


# **13.** Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

# In[52]:


df.loc['k']=['snake',2.0,2,'yes']
print(df)


# In[54]:


df.drop('k')


# **14.** Count the number of each type of animal in `df`.

# In[58]:


df['animal'].count()


# **15.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

# In[61]:


df.sort_values(by=['age','visits'],ascending=[False,True])


# **16.** The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

# In[62]:


df.replace({'priority':{'yes':True,'no':False}})


# **17.** In the 'animal' column, change the 'snake' entries to 'python'.

# In[69]:


df.rename(columns={'animal':'python'})


# **18.** Load the ny-flights dataset to Python

# In[73]:


data=pd.read_csv(r'C:\Users\user\Desktop\ny-flights.csv')
data.head()


# In[76]:


data


# **19.** Which airline ID is present maximum times in the dataset

# In[78]:


data.max()['airline_id']


# **20.** Draw a plot between dep_delay and arr_delay

# In[79]:


import matplotlib.pyplot as plt


# In[82]:


plt.scatter(data['dep_delay'],data['arr_delay'])
plt.title('plot between dep delay and arr delay')
plt.xlabel('dep delay')
plt.ylabel('arr delay')
plt.show()

