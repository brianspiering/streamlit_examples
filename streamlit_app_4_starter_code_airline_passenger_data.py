"""
Plot airline passengers over time.

Complete each TODO to create a working streamlit app.
"""

import streamlit as st
import pandas as pd


# TODO: Add a title for the web app


# TODO: Add a short text description what the web app does


# Load data is done for you
url = "https://raw.githubusercontent.com/brianspiering/datasets/main/airline_passenger_data.csv"
df = pd.read_csv(url)

# TODO: Create sliders for start index and number of months
start_index = None 
n_months  = None

# Select just the rows and single column to plot
data = df.iloc[start_index:start_index+n_months, 2]]

# TODO: Create a line chart of the data

