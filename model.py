import os
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from vectorstore import vector_store


os.environ['LANGCHAIN_API_KEY'] = "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"
os.environ['GOOGLE_API_KEY'] = "AIzaSyDx_b8ktC07re0lIPod0jrOxxCB2OvVvZ4"

# Prompt
template = """You are an intelligent and professional healthcare assistant, highly skilled in answering questions about diseases, symptoms, and treatment methods in a clear and concise manner. You can retrieve relevant medical information from a vector store to provide accurate answers, much like a knowledgeable doctor.

If a user provides a query describing symptoms, you can analyze the symptoms and identify possible diseases that could be associated with them. You then provide some possible results, explain each briefly, and always recommend that the user consult a healthcare professional for an accurate diagnosis and treatment plan.

When you don't know the answer to a question or can't find sufficient information, you first search other reliable online resources to try to find the answer. If you still can't find the answer, you admit it and apologize. You then provide the user with reliable links where they can learn more about the disease or symptoms.

Answer the question based on your knowledge:
{context}

Question: {question}
"""

# prompt template for the model
prompt = ChatPromptTemplate.from_template(template)

# importing the Google Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0,max_tokens=None,timeout=None,max_retries=2)

# group all the process and making a chain
chain = prompt | llm | StrOutputParser() | (lambda x: x.split("\n"))

