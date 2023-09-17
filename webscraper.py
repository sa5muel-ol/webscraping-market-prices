import datetime as date
import re

import pandas as pd
import requests


def scrap_market_data(all_links, dataset):
    # Initialize an empty DataFrame
    all_prices = pd.DataFrame()

    # Loop through the URLs and scrape market data
    for link in all_links:
        response = requests.get(link)

        # Extracting the table with market prices
        prices = pd.read_html(str(response.text))
        df = pd.DataFrame(prices[0])

        # Get the current date
        current_date = date.date.today()

        # Adding Date and Market columns
        df['Date'] = current_date

        # Define a regular expression pattern to match and extract the market names
        pattern = r"http://agromarketday.com/markets/[0-9]+-(.+)-market"
        market_name = re.search(pattern, link).group(1)
        df['Market'] = market_name.capitalize()

        all_prices = pd.concat([all_prices, df], ignore_index=True)

    # Display the updated dataset
    return all_prices
