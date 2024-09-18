# Experiment 3: Python Data Analysis

# I. Intended Learning Outcomes:
  1. To identify the codes and functions incorporated in the Pandas library
  2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library
# II. Instructions:
 Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.
 
## Problem 1
### Instructions:
Using knowledge obtained from the experiment and demonstrations: <br>
a. Load the corresponding .csv file into a data frame named cars using pandas <br>
b. Display the first five and last five rows of the resulting cars. <br>

```python
# 1. Import pandas library into python.
import pandas as pd #To access Pandas library

#A. Load the corresponding .csv file into a data frame named cars using pandas
# 2.  Load the CSV file named cars.csv into your Python environment using the pandas library.
# After loading the cars.csv file into the same folder as this Jupyter notebook, use the pandas library to read the file. Execute the following command to load the data into a DataFrame.
cars = pd.read_csv('cars.csv') #To read the file in the same folder as this notenook
cars

#B. Display the first five and last five rows of the resulting cars.
# 3. Display the first 5 rows of the data set.
# You can view the first five rows using cars.head()
cars.head() #To get the first 5

# 4. Display the last 5 rows of the data set.
# Similar to the head function, To view the last five rows of the data set use cars.tail()
cars.tail() #To get the last 5

```
### PROBLEM 2: 

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

```python

import pandas as pd #To access Pandas library

cars = pd.read_csv('cars.csv') #To read the file in the same folder as this notebook
cars

#A. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
cars.iloc[:, 0::2].head()

#B. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
cars.loc[cars['Model'] == 'Mazda RX4']

#C. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]

#D. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]




