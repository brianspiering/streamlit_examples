"""
Example of a straightforward Streamlit app
"""

import streamlit as st


st.title("Simulation")
st.write("'We have to realize that computers are simulators and then figure out what to simulate.' \n\n — Alan Kay")

trend = st.slider('Trend',  min_value=0.001, max_value=0.10, step=0.01)
noise = st.slider('Noise',min_value=0.01,  max_value=0.10, step=0.01)

st.write(f"Trend = {trend} \n\n Noise = {noise}")