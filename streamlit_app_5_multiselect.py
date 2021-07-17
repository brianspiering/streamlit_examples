"""
Visualize Big Mac dataset

- Add multi-select for country
- Add single-select for currency
"""

import streamlit as st
import pandas as pd


st.title('Big Mac Index by Country')

# |       date | currency_code | name      | local_price | dollar_ex | dollar_price |
# | ---------- | ------------- | --------- | ----------- | --------- | ------------ |
# | 2000-04-01 | ARS           | Argentina | 2.500…      | 1.000…    |  2.500…      |
# | 2000-04-01 | AUD           | Australia | 2.590…      | 1.680…    | 1.542…       |
# | 2000-04-01 | BRL           | Brazil    | 2.950…      | 1.790…    | 1.648…       |

def load_data():
    url = "https://raw.githubusercontent.com/TheEconomist/big-mac-data/master/output-data/big-mac-adjusted-index.csv"
    data = pd.read_csv(url)
    return data.assign(date=lambda d: pd.to_datetime(d['date']))

df = load_data()

countries = st.sidebar.multiselect(
    "Select Countries",
    df['name'].unique()
)

price_type = st.sidebar.selectbox(
    "Select Column",
    ("local_price", "dollar_price")
)

subset_df = df.loc[lambda d: d['name'].isin(countries)]

for name in countries:
    # Select row
    current_df = subset_df.loc[lambda d: d['name'] == name]
    # Select column
    current_df = current_df[price_type]
    # Plot
    st.line_chart(current_df)

if st.sidebar.checkbox("Show Raw Data"):
    st.markdown("### Raw Data")
    st.write(subset_df) # Multiple dispatch - change options based on type
