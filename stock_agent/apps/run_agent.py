from stock_agent.pkg.implementation.polygon import PolygonTools
import os
from dotenv import load_dotenv


# run main:
if __name__ == "__main__":
    # you would keep taking the users input from cmd line and keep runing your code
    agent = PolygonTools(llm_company_name="OpenAI", model_llm_name="gpt-5-nano-2025-08-07")    

    # 1.) create infinite loop till the user exits
    # 2.) for each iteration take the users question from the cmd line
    # 3.) take that question and run it through your LLM -> call a tool if needed -> tool function will call the API -> return to the llm and the LLM would take the question of the user and the data from the API and answer the question
    print()
    print("Welcome to Arjun's stock companion. Asks a question to get an intelligent response based on real time data!\n")
    print("You can quit or close the program by typing '//Q' ")
    
    while True:
        userquery = input()   
        if (userquery.lower() == "//q"):
            break            
        else:
            print(agent.run(userquery))