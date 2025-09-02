from stock_agent.pkg.types.base_agent import BaseStockAgent


class PolygonTools(BaseStockAgent):
    def get_current_price(self, ticker_name: str) -> float:
       return 12.0

    def get_today_close_open_price(self, ticker_name: str) -> float:
        return 6.0