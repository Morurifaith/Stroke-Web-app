# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
#loading the saved model
loaded_model=pickle.load(open('C:/Users/ALVIN/Desktop/Deploying ML model/Stroke_Prediction.sav', 'rb'))                          
                              
input_data=(0,78,0,0,1,100.9,30.5,0,0,1,0,0,0,1,0,1,0,0)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
    print('The person has a risk of getting stroke')
else:
    print('The person has no risk of getting stroke')                              