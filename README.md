# HDSC-21-SCIPY-GROUP

# Repository for the Scipy Members

## Problem Statement
The Times Higher Education World University Rankings 2021 include more than 1,500 universities across 93 countries and regions, making them the largest and most diverse university rankings to date.
We are tasked with creating an automated system to estimate which university ranks the best given the world university ranking using calibrated performance indicators that measure an institution’s performance such as  teaching, research, knowledge transfer and international outlook.
Estimates from our system will be used to in providing young people and their families with trusted guidance to help with academic decisions

## Tasks breakdown
1.  Extract the data from https://www.timeshighereducation.com/world-university-rankings/2013/world-ranking/detailed#!/page/0/length/25/sort_by/[…]rt_order/asc/cols/undefined
 
2.  on the page we have data from 2011 to 2021 and i think we should explore from 2016 till date
 
3.  We need to create a column that shows the years for our data
 
 4. FILL n/a
 
 5. we need to merge the data into one file
 
 6. the there are two tables ranks and scores, we need to extract both tables
 
 7. after extracting the table, there is a column called "Rank", this is our target column so we need to drop this column
 
 8. we need to split the Female: Male ratio column
 
 9. We need to split the Name/Country/Region Column
 
 10. other columns are our input columns for training
 
 11. we need to scale our numerical columns(we can use min max scaler)
 
 12. we need to encode our categorical columns( we can use one hot encoder)
 
 13. after which we can decide on the machine learning model to use( I think we have a regression problem)
 
 14. we fit the model
 
 15. train the model
 
 16. make predictions
 
 17. and lastly we deploy and interpret our model 
 
 N.B: the list above is not exhaustive, its subject to modifications and corrections
