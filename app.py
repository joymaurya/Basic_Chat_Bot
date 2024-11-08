import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful assistant give answer to queries with best of your abilites"),
        ("human","{question}")
    ]
)
parser=StrOutputParser()
def get_response(message,model,temperature,max_tokens,api_key):
    Model=ChatGroq(model=model,api_key=api_key,temperature=temperature,max_tokens=max_tokens)
    chain=prompt|Model|parser
    response=chain.invoke({"question":message})
    return response
api_key=st.sidebar.text_input(label="GROQ_API_KEY")
model=st.sidebar.selectbox(label="Select GROQ Model",options=["llama3-8b-8192","llama3-70b-8192","mixtral-8x7b-32768"])
temperature=st.sidebar.slider(label="Temperature",max_value=2,min_value=0,value=1)
max_tokens=st.sidebar.slider(label="Max_Tokens",max_value=8192,min_value=0,value=1024)
question=st.text_input(label="Write your question Here")
if question:
    st.write(get_response(question,model,temperature,max_tokens,api_key))