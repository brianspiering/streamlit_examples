"""
Plot airline passengers over time.

Complete each TODO to create a working streamlit app.
"""

import streamlit as st
import pandas as pd


# TODO: Add a title for the web app


# TODO: Add A short piece of text describing what the web app does


# Load data is done for you
url = "https://raw.githubusercontent.com/brianspiering/datasets/main/airline_passenger_data.csv"
df = pd.read_csv(url)

# TODO: Create sliders for the stop and start indices


# Select out just the rows and single column to plot is done for you.
data = df.iloc[start_index:stop_index, 2]

# TODO: Create a line chart of the data

