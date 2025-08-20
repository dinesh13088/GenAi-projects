from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding_model=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents=[
  "Diabetes is a chronic condition where the body cannot properly process glucose.",
  "Kathmandu City Hospital offers online appointment booking for all departments.",
  "Common symptoms of flu include fever, cough, sore throat, and body aches.",
  "Dr. Dinesh Tamang is a cardiologist available Monday to Friday at HealthMate Clinic.",
  "Patients are advised to drink plenty of water and rest when experiencing dehydration."
]
query="tell me about diabetes"

doc_embedding=embedding_model.embed_documents(documents)
query_embedding=embedding_model.embed_query(query)
## [query_embedding] is done because doc_embedding is 2d list of embedding
cosine_sim=cosine_similarity([query_embedding],doc_embedding)[0]

##it sorts based on the value of the enum list --> x[1]=values and x[0] contains enum value like 0,1,2..
index,score=sorted(list(enumerate(cosine_sim)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarities score is:",score)