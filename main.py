import datetime as date

import pandas as pd
import streamlit as st

from webscraper import scrap_market_data

st.write('Weekly Market Prices')

# Define the column headers
columns = ["Commodity", "Price", "Units", "Date", "Market"]

# Create an empty DataFrame with the specified columns
data = pd.DataFrame(columns=columns)
current_date = date.datetime.now()

# Define the file path for the CSV file in the user's Downloads folder
csv_file_path = f"{current_date} Market Prices.csv"

# List of market URLs
links = [
    "http://agromarketday.com/markets/1-mbale-central-market",
    "http://agromarketday.com/markets/2-jinja-central-market",
    "http://agromarketday.com/markets/3-lira-main-market",
    "http://agromarketday.com/markets/4-kiboga-main-market",
    "http://agromarketday.com/markets/5-nakasero-market",
    "http://agromarketday.com/markets/6-kalerwe-market",
    "http://agromarketday.com/markets/7-soroti-main-market",
    "http://agromarketday.com/markets/8-iganga-main-market",
    "http://agromarketday.com/markets/9-nakawa-market",
    "http://agromarketday.com/markets/11-kabale-main-market",
    "http://agromarketday.com/markets/12-owino-market",
    "http://agromarketday.com/markets/13-arua-main-market",
    "http://agromarketday.com/markets/14-gulu-main-market"
]

with st.sidebar:
    st.write('Download Recent Price Information')

    if st.button('Refresh data'):
        data = scrap_market_data(dataset=data, all_links=links)
        st.write('Success')

    if not data.empty:
        data_as_csv = data.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download data as CSV",
            data_as_csv,
            csv_file_path,
            "text/csv",
            key="download-tools-csv",
        )

if not data.empty:
    st.write('Preview Market Prices as at ', current_date)
else:
    st.write('Preview Market Prices')

st.write(data)
