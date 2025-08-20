from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
llm=HuggingFaceEndpoint(repo_id='', task="text-generation")
model=ChatHuggingFace(llm)
model.invoke("what is your name ")