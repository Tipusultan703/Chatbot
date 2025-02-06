import streamlit as st  
from langchain_openai import ChatOpenAI  
from langchain_experimental.sql import SQLDatabaseChain  
from langchain_community.utilities import SQLDatabase  
import openai  
import os  
from dotenv import load_dotenv  
from langchain_helper import get_few_shot_db_chain  

load_dotenv()

#api key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# credentials
db_user = "root"
db_password = ""  
db_host = "localhost"
db_name = "atliq_tshirts"

# Connect to the database
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)


llm = ChatOpenAI(model_name="gpt-3.5-turbo")

 
db_chain = get_few_shot_db_chain(llm, db, verbose=True) 

# Streamlit app setup
st.title("Atliq T-Shirts: Database Q&A")  # Title of the app
question = st.text_input("Enter your question") 


if question:
    with st.spinner("Processing..."):  
        response = db_chain.invoke(question)  
        st.success("Done!") 
        st.write(response)  # Display the response





