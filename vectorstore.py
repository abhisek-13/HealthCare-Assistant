import os
import pickle
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_cohere import CohereEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

os.environ['COHERE_API_KEY'] = "tnn72dLZ0ntWutFeQIrxUsPRJ2cA9Du7adub6thE"


# PDF List
pdf_files = ['Resources\CMDT-2022.pdf', 
              'Resources\CMDT-2023.pdf',
              'Resources\medical_book.pdf',
              'Resources\The_Merck_Manual_of_Diagnosis_and_Therap.pdf']
  
# Initialize a list to hold all documents
fetch_text = []
  
# Load each PDF and append its documents to the list
for pdf_file in pdf_files:
  loader = PyPDFLoader(pdf_file)
  documents = loader.load()
  fetch_text.extend(documents)
  
# Split the content
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  chunk_size=1000,
  chunk_overlap=50)
splits = text_splitter.split_documents(fetch_text)
  
# Index the content
vectorstore = Chroma.from_documents(
  documents=splits,
  embedding=HuggingFaceEmbeddings())
  


# Setup the retriever
# retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
  

