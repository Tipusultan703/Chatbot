# langchain_helper.py

from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.llms import OpenAI  # Updated import statement
from pydantic import BaseModel  # Import BaseModel

# Define a BaseCache class
class BaseCache(BaseModel):
    cache_key: str
    cache_value: str

# Define a Callbacks class if necessary
class Callbacks(BaseModel):
    callback_key: str

# Ensure SQLDatabaseChain is fully defined
SQLDatabaseChain.model_rebuild()

def get_few_shot_db_chain(llm, db, verbose=True):

    
    return SQLDatabaseChain.from_llm(llm, db, verbose=verbose)



