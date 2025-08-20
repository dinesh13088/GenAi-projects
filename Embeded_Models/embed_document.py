from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
documents=[
    "Dinesh is a good boy",
    "kathmandu is capital city of nepal",
    "Dinesh studies very hard"
]
embedding_model=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

result=embedding_model.embed_documents(documents)
print(str(result))