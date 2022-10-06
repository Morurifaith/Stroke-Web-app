# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:17:20 2022

@author: ALVIN
"""

import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('C:/Users/ALVIN/Desktop/Deploying ML model/Stroke_Prediction.sav', 'rb'))

#creating a function

def stroke_pred(input_data):
    
    
    input_data_as_numpy_array=np.asarray(input_data)
    
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
        return 'The person has a risk of getting stroke'
    else:
        return 'The person has no risk of getting stroke'


def main():
    
    #giving a title
    st.title('Stroke Risk Prediction Web App')

    #getting the input data from the user
    #'gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
    #'avg_glucose_level', 'bmi', 'stroke', 'work_type_Govt_job',
    #'work_type_Never_worked', 'work_type_Private',
    #'work_type_Self-employed', 'work_type_children', 'Residence_type_Rural',
    #'Residence_type_Urban', 'smoking_status_Unknown',
    #'smoking_status_formerly smoked', 'smoking_status_never smoked',
    #'smoking_status_smokes'
    gender=st.text_input('0 for male and 1 for female')
    age=st.text_input('Age')
    hypertension=st.text_input('whether they had hypertension before')
    heart disease=st.text_input('whether they have a heart disease')
    ever_married=st.text_input('whether they have been married before')
    avg_glucose_level=st.text_input('the average glucose levels')
    bmi=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
    heart disease=st.text_input('whether they have a heart disease')
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    