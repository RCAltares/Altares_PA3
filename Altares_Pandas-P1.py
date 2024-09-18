#!/usr/bin/env python
# coding: utf-8

# #### Problem 1
# 

# #### 1. Import pandas library into python.

# In[47]:


import pandas as pd #To access Pandas library


# #### 2.  Load the CSV file named cars.csv into your Python environment using the pandas library.
# ##### After loading the cars.csv file into the same folder as this Jupyter notebook, use the pandas library to read the file. Execute the following command to load the data into a DataFrame.

# In[61]:


cars = pd.read_csv('cars.csv') #To read the file in the same folder as this notenook
cars


# #### 3. Display the first 5 rows of the data set.
# #####  You can view the first five rows using cars.head()

# In[51]:


cars.head() #To get the first 5


# #### 4. Display the last 5 rows of the data set.
# ##### Similar to the head function, To view the last five rows of the data set use cars.tail()

# In[53]:


cars.tail() #To get the last 5

