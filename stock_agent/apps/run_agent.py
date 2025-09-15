from stock_agent.pkg.implementation.polygon import PolygonTools
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
import datetime


# run main:
if __name__ == "__main__":
    agent = PolygonTools(llm_company_name="OpenAI", model_llm_name="gpt-5-nano-2025-08-07")    
    
    # Welcome users to the Agent
    print("\nWelcome to Arjun's stock companion. Ask a question to get an intelligent response based on real time data!\n\n" + 
    "You can quit or close the program by typing '//Q'")
    
    today = datetime.datetime.now()
    messages = [
            SystemMessage(content=("You are a helpful AI Agent, providing financial insight on stock related " 
           f"queries try to provide insights on top of serving data. Today's date is: {today}. " 
            "Use the tools you have access to as needed but note you do not have the abillity to interact with " 
            "links and the open internet."))
            ]

    while True:
        print("Your Query: ", end="")
        userquery = input()

        if (userquery.lower() == "//q"):
            break            
        else:
            messages.append(HumanMessage(content=userquery))
            messages = agent.run(messages)
            response = messages[-1].content.strip()
            print(response)