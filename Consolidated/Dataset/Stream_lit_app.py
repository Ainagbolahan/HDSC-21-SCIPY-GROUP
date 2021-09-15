#!/usr/bin/env python
# coding: utf-8

# In[1]:


#np.array( [[scaled_features]].values.reshape(-1, 1)


# In[3]:


import pickle
import streamlit as st
import numpy as np

# loading the trained model
pickle_in = open('svr_model.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(No_of_FTE_Students, No_of_students_per_staff,International_Students, Teaching, Research, Citations,
       Industry_Income, International_Outlook,Year):



# Making predictions 
    prediction = classifier.predict(np.array([[No_of_FTE_Students, No_of_students_per_staff,International_Students, Teaching, Research, Citations,
       Industry_Income, International_Outlook,Year]]) )
    if prediction <= 0:
        pred = 'Confirm Accuracy of your data'
    else:
        pred = 'Your Rank Score is {}'.format(prediction)
    return pred


#this is the main function in which we define our webpage  
def main(): 
    
#front end elements of the web page 

    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit University Ranking ML App</h1> 
    </div> 
    """

#display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

#following lines create boxes in which user can enter data required to make prediction 
    No_of_FTE_Students = st.number_input("No_of_FTE_Students")
    No_of_students_per_staff = st.number_input("No_of_students_per_staff")
    International_Students = st.number_input('International_Students')
    Teaching = st.number_input("Teaching")
    Research = st.number_input("Research")
    Citations = st.number_input("Citations")
    Industry_Income = st.number_input("Industry_Income")
    International_Outlook = st.number_input("International_Outlook")  
    Year = st.number_input("Year") 
     
    result =""

#when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(No_of_FTE_Students, No_of_students_per_staff,
           International_Students, Teaching, Research, Citations,
           Industry_Income, International_Outlook,Year) 
        st.success('Your Rank Score is {}'.format(result))


if __name__=='__main__': 
    main()


# In[ ]:





# In[ ]:




