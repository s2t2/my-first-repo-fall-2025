
import os

from pandas import read_csv
from dotenv import load_dotenv
import plotly.express as px

load_dotenv() # loads environment variables from the ".env" file

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def fetch_stocks_csv(symbol="NFLX"):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    stocks_df = read_csv(request_url)
    return stocks_df


if __name__ == "__main__":

    # FETCH THE DATA

    symbol = input("Please choose a stock symbol: ") or "NFLX"

    stocks_df = fetch_stocks_csv(symbol)
    print(stocks_df.head())

    # CHART THE DATA

    fig = px.line(stocks_df, x="timestamp", y="adjusted_close",
                title=f"Stock Prices ({symbol})",
                height=450
                )
    fig.show()
