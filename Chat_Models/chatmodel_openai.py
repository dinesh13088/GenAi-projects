from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
chat_model=ChatOpenAI(model='gpt-4')
result=chat_model.invoke('what is the capital of nepal?')
##the result in chatmodels contents the meta data of the result so.. to display the content
##it has content key
print(result.content)