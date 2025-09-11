from stock_agent.pkg.implementation.polygon import PolygonTools
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage


# run main:
if __name__ == "__main__":
    agent = PolygonTools(llm_company_name="OpenAI", model_llm_name="gpt-5-nano-2025-08-07")    

    # Welcome users to the Agent
    print("\nWelcome to Arjun's stock companion. Ask a question to get an intelligent response based on real time data!\n\n" + 
    "You can quit or close the program by typing '//Q'")
    
    messages = [
            SystemMessage(content="You are a helpful stock assistant. Use tools when needed."),
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