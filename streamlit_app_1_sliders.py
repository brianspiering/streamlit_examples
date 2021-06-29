"""
Example of a straightforward Streamlit app
"""

import streamlit as st


st.title("Simulation")
st.write("We have to realize that computers are simulators and then figure out what to simulate. — Alan Kay")

intercept = st.slider('Intercept', min_value=1, max_value=1000, step=1)
slope = st.slider('Slope', min_value=1, max_value=100, step=1)

st.write(f"Intercept={intercept} \n\n Slope={slope}")
