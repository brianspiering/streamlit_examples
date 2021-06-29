"""
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulation")
st.write("'We have to realize that computers are simulators and then figure out what to simulate.' \n\n — Alan Kay")

trend = st.slider('Trend',  min_value=0.001, max_value=0.10, step=0.01)
noise = st.slider('Noise',min_value=0.01,  max_value=0.10, step=0.01)
st.write(f"Trend = {trend} \n\n Noise = {noise}")

intial_value = 1
n_series = 10 
time_series = np.cumprod(intial_value + np.random.normal(rate, noise, (100, n_series)), 
                         axis=0)

fig, ax = plt.subplots()
for ts in time_series.T:
    ax.plot(ts)

st.pyplot(fig)
