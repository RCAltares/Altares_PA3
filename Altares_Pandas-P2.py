#!/usr/bin/env python
# coding: utf-8

# #### Problem 2
# 

# #### 1. Import pandas library into python.

# In[1]:


import pandas as pd #To access Pandas library


# #### 2.  Load the CSV file named cars.csv into your Python environment using the pandas library.
# ##### After loading the cars.csv file into the same folder as this Jupyter notebook, use the pandas library to read the file. Execute the following command to load the data into a DataFrame.

# In[3]:


cars = pd.read_csv('cars.csv') #To read the file in the same folder as this notebook
cars


# #### 3. Display the First Five Rows with Odd-Numbered Columns
# ##### Use iloc for position-based indexing, selecting every second column (1st, 3rd, 5th, etc.).
# ##### Using .head() to show only the first five rows.

# In[29]:


cars.iloc[:, 0::2].head()


# #### 4. Display the row that contains the 'Model' of 'Mazda RX4'
# ##### Using loc for label-based indexing, you can specify the condition within the brackets.

# In[31]:


cars.loc[cars['Model'] == 'Mazda RX4']


# #### 5. How many cylinders ('cyl') does the car model 'Camaro Z28' have?
# ##### To specify both the row condition and the column label with loc.

# In[39]:


cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]


# #### 6. To Determine how many cylinders ('cyl') and what gear type ('gear') the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.
# ##### Use loc to filter for multiple models and specify the columns 'cyl' and 'gear'.

# In[43]:


cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]

