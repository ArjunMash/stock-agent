from abc import ABC, abstractmethod


class BaseStockAgent(ABC):
    def __init__(self, llm_company_name: str, model_llm_name:str):
        self.llm_company_name = llm_company_name
        self.model_llm_name = model_llm_name
        # create llm using langchain
        # TODO: use lanchaing to create the self.langchain (model, company whatever)


    def run(self, user_query: str) -> str:
        # 1.) call the llm with user query:
        # 2.) see if there is an an llm tool call
        # 3.) if yes (get_current_price llm will also provide you the input -> APPL, get_today_close_open_price)
        price = user_query
        if "get price" in user_query:
            price = self.get_current_price(user_query)
        if "today open" in user_query:
            price = self.get_today_close_open_price(user_query)
        return price


    @abstractmethod
    def get_current_price(self, ticker_name: str) -> float:
        pass

    @abstractmethod
    def get_today_close_open_price(self, ticker_name: str) -> float:
        pass


