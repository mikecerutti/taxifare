import streamlit as st

"""
# Taxi Fare Prediction
"""

pu_date = st.date_input('Pick-up Date', value=date.today())
pu_time = st.time_input('Pick-up Time', value=datetime.time(12))
pu_lat = st.number_input('Pick-up Latitude', value=40.165220)
pu_long = st.number_input('Pick-up Longitude' value=-83.062350)
du_lat = st.number_input('Drop-off Latitude', value=39.997520)
du_long = st.number_input('Drop-off Longitude', value=83.004260)
nb_px = st.number_input('Passenger Count', value=1, min_value=1, max_value=12)
