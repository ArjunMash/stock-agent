from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool


class BaseStockAgent(ABC):
    def __init__(self, llm_company_name: str, model_llm_name:str):
        load_dotenv()
        os.environ.get("OPENAI_API_KEY")
        
        # Define tools
        @tool        
        def get_ticker_price(ticker_name: str) -> str:
            """Return OHLC stock data for a ticker as a JSON string."""
            return self.get_ticker_price(ticker_name)

        @tool
        def get_ticker_desc(ticker_name: str) -> str:
            """Return an overview of information about a company as a JSON string."""
            return self.get_ticker_desc(ticker_name)             

        tools = [get_ticker_price,get_ticker_desc]

        self.llm = init_chat_model(model_llm_name, model_provider= llm_company_name)
        self.llm_with_tools = self.llm.bind_tools(tools)
    
    def run(self, user_query: str) -> str:        
        # System prompt   
        messages = [
            SystemMessage(content="You are a helpful stock assistant. Use tools when needed."),
            HumanMessage(content=user_query),
        ] 

        ai_msg = self.llm_with_tools.invoke(messages)
        
        # Loop through tool calls and pass requests to Polygon
        messages.append(ai_msg)
        for tool_call in ai_msg.tool_calls:
            selected_tool = {"get_ticker_price": self.get_ticker_price, "get_ticker_desc": self.get_ticker_desc}[tool_call["name"].lower()]
            args = tool_call["args"]
            tool_output = selected_tool(**args)
            tool_output = str(tool_output)            
            messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
        messages 

        # Finally return LLMs final formatted response
        return self.llm_with_tools.invoke(messages).content.strip()           

    # Abstract methods outlining requirments for tool calls implementations need to have    
    @abstractmethod
    def get_ticker_price(self, ticker_name: str) -> str:
        pass

    @abstractmethod
    def get_ticker_desc(self, ticker_name: str) -> str:
        pass
