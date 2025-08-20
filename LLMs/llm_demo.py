from langchain_openai import OpenAI
from dotenv import load_dotenv

##it loads the api key from the environment variables
load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')
reply=llm.invoke("What is the capital of Nepal?")

print(reply)