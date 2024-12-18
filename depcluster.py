# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:10:35 2024

@author: Abhinay
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading the saved model
loaded_model = pickle.load(open(r"C:\Users\HP\Desktop\Data Science\projects\model_kmeans", 'rb'))

def Cluster_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'Developing Country'
    elif (prediction[0] == 1):
        return 'Developed Country'
    else:
        return 'Under Developed Country'  

def main():
    # giving a title
    st.title('Cluster Prediction')

    # Input fields with adjustable values using buttons
    Birth_Rate = st.number_input('Enter birth rate', min_value=0.0, max_value=100.0, value=10.0, step=0.1)
    Business_Tax_Rate = st.number_input('Enter tax Percentage', min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    CO2_Emissions = st.number_input('CO2 Emissions (in metric tons)', min_value=0.0, max_value=100000.0, value=150.0, step=1.0)
    Days_to_Start_Business = st.number_input('Enter Number of days to start business', min_value=1, max_value=365, value=30, step=1)
    Ease_of_Business = st.number_input('Ease of Business (scale 1-10)', min_value=1, max_value=10, value=7, step=1)
    Energy_Usage = st.number_input('Total Energy Usage (MWh)', min_value=0.0, max_value=100000.0, value=5000.0, step=10.0)
    GDP = st.number_input('Total GDP (in Billion $)', min_value=0.0, max_value=1000000.0, value=25000.0, step=100.0)
    Health_Exp_Capita = st.number_input('Total Health expenditure per capita (in $)', min_value=0.0, max_value=20000.0, value=2000.0, step=10.0)
    Hours_to_do_Tax = st.number_input('Hours to do Tax (per year)', min_value=0.0, max_value=1000.0, value=100.0, step=1.0)
    Infant_Mortality_Rate = st.number_input('Infant Mortality Rate in Percentage', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    Internet_Usage = st.number_input('Average Internet Usage (Percentage)', min_value=0.0, max_value=100.0, value=75.0, step=1.0)
    Lending_Interest = st.number_input('Lending Interest Rate (Percentage)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    Life_Expectancy_Female = st.number_input('Life Expectancy Female (Years)', min_value=0.0, max_value=120.0, value=75.0, step=1.0)
    Life_Expectancy_Male = st.number_input('Life Expectancy Male (Years)', min_value=0.0, max_value=120.0, value=70.0, step=1.0)
    Mobile_Phone_Usage = st.number_input('Mobile Phone Usage (Percentage)', min_value=0.0, max_value=100.0, value=80.0, step=1.0)
    Population_0_14 = st.number_input('Total population between 0-14 in percentage', min_value=0.0, max_value=100.0, value=20.0, step=1.0)
    Population_15_64 = st.number_input('Total population between 15-64 in percentage', min_value=0.0, max_value=100.0, value=60.0, step=1.0)
    Population_65_and_above = st.number_input('Total population above 65 in percentage', min_value=0.0, max_value=100.0, value=10.0, step=1.0)
    Population_Total = st.number_input('Total population', min_value=0, max_value=1000000000, value=100000000, step=1000000)
    Population_Urban = st.number_input('Urban population in percentage', min_value=0.0, max_value=100.0, value=60.0, step=1.0)
    Tourism_Inbound = st.number_input('$ earned in tourism (in million $)', min_value=0.0, max_value=100000.0, value=2000.0, step=10.0)
    Tourism_Outbound = st.number_input('$ spent on tourism (in million $)', min_value=0.0, max_value=100000.0, value=1500.0, step=10.0)

    # code for Prediction
    Predict = ''
    
    # creating a button for Prediction
    if st.button('Submit'):
        input_data = [
            Birth_Rate, Business_Tax_Rate, CO2_Emissions, Days_to_Start_Business, Ease_of_Business,
            Energy_Usage, GDP, Health_Exp_Capita, Hours_to_do_Tax, Infant_Mortality_Rate, Internet_Usage,
            Lending_Interest, Life_Expectancy_Female, Life_Expectancy_Male, Mobile_Phone_Usage,
            Population_0_14, Population_15_64, Population_65_and_above, Population_Total, Population_Urban,
            Tourism_Inbound, Tourism_Outbound
        ]
        Predict = Cluster_prediction(input_data)

    st.success(Predict)
    
if __name__ == '__main__':
    main()
