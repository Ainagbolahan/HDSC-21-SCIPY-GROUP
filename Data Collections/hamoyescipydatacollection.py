# -*- coding: utf-8 -*-
"""HamoyeSciPyDataCollection.ipynb

 Data Collection Task
"""

#Importing required libraries
import numpy as np
import pandas as pd

#Function to add the specified year to the table which were downloaded individually.
def addyear(input):
  #input is the column used in the expression to create the required year for the data
  if input != None:
    global year
    year = year
  return year

#Function to import the required datasets and merge the data using an inner join on Country/Region name.
def mergecolumns(data_1, data_2, column, name):
  #data_1 holds value for table containing information about the numbers of students
  #data_2 holds value for the table containing information about the rank and scores.
  df1 = pd.read_csv(data_1)
  df2 = pd.read_csv(data_2)
  df = pd.merge(df1, df2, on=column)
  df.to_csv(name + ".csv", index=False)

table1 = ["wur_2021.csv", "wur_2020.csv", "wur_2019.csv", "wur_2018.csv", "wur_2017.csv", "wur_2016.csv"]
table2 = ["times-higher-edu-2021.csv", "times-higher-edu-2020.csv", "times-higher-edu-2019.csv", "times-higher-edu-2018.csv", "times-higher-edu-2017.csv", "times-higher-edu-2016.csv"]
lab = ["wur_2021", "wur_2020", "wur_2019", "wur_2018", "wur_2017", "wur_2016"]

for i in range(len(table1)):
  mergecolumns(table1[i], table2[i], "NameCountry/Region", lab[i])

def useyear(name, yr):
  global year
  year = yr
  df = pd.read_csv(name)
  df["Year"] = df["NameCountry/Region"].apply(addyear)
  df.to_csv(name, index=False)

for i in range(len(table1)):
  useyear(table1[i], lab[i][4:])

#append tables
df1 = pd.read_csv("wur_2021.csv")
df2 = pd.read_csv("wur_2020.csv")
df3 = pd.read_csv("wur_2019.csv")
df4 = pd.read_csv("wur_2018.csv")
df5 = pd.read_csv("wur_2017.csv")
df6 = pd.read_csv("wur_2016.csv")

df1 = df1.append(df2)
df1 = df1.append(df3)
df1 = df1.append(df4)
df1 = df1.append(df5)
df1 = df1.append(df6)

df1.to_csv("Wurld2016_2021.csv", index=False)

data = pd.read_csv("Wurld2016_2021.csv")
len(data.index)

