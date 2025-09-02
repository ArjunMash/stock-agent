from stock_agent.pkg.implementation.polygon import PolygonTools
import os
from dotenv import load_dotenv


load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")


# run main:
if __name__ == "__main__":
    # you would keep taking the users input from cmd line and keep runing your code
    agent = PolygonTools(llm_company_name="OpenAI", model_llm_name="GPT 5")
    # 1.) create infinite loop till the user exits
    # 2.) for each iteration take the users question from the cmd line
    # 3.) take that question and run it through your LLM -> call a tool if needed -> tool function will call the API -> return to the llm and the LLM would take the question of the user and the data from the API and answer the question
    
    # Step one initialize Langchain and get the user able to prompt the bot through CLI

    userquery = "get price of APPL price"
    print(agent.run(userquery))

    userquery = "today open"
    print(agent.run(userquery))

    userquery = "price of blah"
    print(agent.run(userquery))