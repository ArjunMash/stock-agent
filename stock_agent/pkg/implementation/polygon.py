from stock_agent.pkg.types.base_agent import BaseStockAgent
from polygon import RESTClient
import os
from dotenv import load_dotenv
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

load_dotenv()
PolygonKey = os.environ.get("PolygonKey")
client = RESTClient(PolygonKey)


class PolygonTools(BaseStockAgent):
    # Get ticker's recent day end results (can only do day close due to free API)
    def get_ticker_price(self, ticker_name: str) -> str:
        aggs = client.get_previous_close_agg(
            ticker_name,
            adjusted="true",
        )
        return(aggs)    

    # Get historic ticker performance
    

    # Get Ticker description
    def get_ticker_desc(self, ticker_name: str) -> str:
        details = client.get_ticker_details(ticker_name)
        return(details)
    
    def get_ticker_fundamentals(self, ticker_name: str)  -> list:
        financials = []
        for f in client.vx.list_stock_financials(
            ticker=ticker_name,
            order="asc",
            limit="10",
            sort="filing_date",
            ):
            financials.append(f)
        


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.show()