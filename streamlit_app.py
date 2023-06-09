import streamlit as st
import requests
import datetime

"""
# Taxi Fare Prediction
"""

pu_date = st.date_input('Pick-up Date', value=datetime.datetime.today())
pu_time = st.time_input('Pick-up Time', value=datetime.time(12))
pu_lat = st.number_input('Pick-up Latitude', value=40.165220)
pu_long = st.number_input('Pick-up Longitude', value=-83.062350)
do_lat = st.number_input('Drop-off Latitude', value=39.997520)
do_long = st.number_input('Drop-off Longitude', value=-83.004257)
nb_px = st.number_input('Passenger Count', value=1, min_value=1, max_value=12)

calc_fare = 0  # Default value

if st.button('Calculate'):
    url = "https://taxifare.lewagon.ai/predict"
    predict_dict = {
        'pickup_datetime': str(pu_date) + " " + str(pu_time),
        'pickup_longitude': pu_long,
        'pickup_latitude': pu_lat,
        'dropoff_longitude': do_long,
        'dropoff_latitude': do_lat,
        'passenger_count': nb_px
    }
    response = requests.get(url, params=predict_dict)
    calc_fare = response.json()['fare']

    formatted_fare = "${:.2f}".format(calc_fare)
    st.header(f"Calculated fare: {formatted_fare}")
