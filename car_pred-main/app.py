import streamlit as st
import pandas as pd
import joblib
#from datetime import datetime

car = pd.read_csv('Carmodel.csv')
model = joblib.load("LinearRegressionModel.pkl")
car_company = ['Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Force', 'Ford',
        'Hindustan', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Land',
        'Mahindra', 'Maruti', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
        'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo']

st.set_page_config('Car Price Prediction', '🚗')
st.title("Car Price Prediction")
st.text("")

car_com = st.selectbox('Select Car company', car_company, help='Enter the name of your car')
car_model = st.selectbox('Select Car model', car[car_com].dropna().values, help='Enter the name of your car model')
car_purchased = st.text_input('Year Purchased', 2005, help='Enter the year the car was purchased')
car_driven = st.slider('Kilometers driven', 1, 100000, help='How much kilometers the car was driven')
car_type = st.selectbox('Select Fuel type', ['Petrol', 'Diesel'], help='Enter fuel type')

st.text("")
predict = st.button("Predict")


if predict:
    model_pred = model.predict(pd.DataFrame([[car_model, car_com, car_purchased, car_driven, car_type]],
                                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    if model_pred[0] > 0:
        txt = 'Predicted Price of ' + car_model + ': ' + ' ₹' + str(int(model_pred[0]))
        st.subheader(txt)
    else:
        txt = "They do not fit in the condition."
        st.subheader(txt)
