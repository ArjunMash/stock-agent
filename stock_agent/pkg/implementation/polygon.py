from stock_agent.pkg.types.base_agent import BaseStockAgent
from polygon import RESTClient
import os
from dotenv import load_dotenv

load_dotenv()
PolygonKey = os.environ.get("PolygonKey")
client = RESTClient(PolygonKey)


class PolygonTools(BaseStockAgent):
    # Get ticker's recent day end results (can only do day close due to free API)
    def get_ticker_price(self, ticker_name: str) -> float:
        aggs = client.get_previous_close_agg(
            ticker_name,
            adjusted="true",
        )
        return(aggs)    

    # Get Ticker description
    def get_ticker_desc(self, ticker_name: str) -> float:
        details = client.get_ticker_details(ticker_name)
        return(details)