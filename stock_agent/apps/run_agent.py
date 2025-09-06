from stock_agent.pkg.implementation.polygon import PolygonTools
import os
from dotenv import load_dotenv


# run main:
if __name__ == "__main__":
    agent = PolygonTools(llm_company_name="OpenAI", model_llm_name="gpt-5-nano-2025-08-07")    

    # Welcome users to the Agent
    print("Welcome to Arjun's stock companion. Ask a question to get an intelligent response based on real time data!\n")
    print("You can quit or close the program by typing '//Q' ")
    
    while True:
        userquery = input()   
        if (userquery.lower() == "//q"):
            break            
        else:
            print(agent.run(userquery))