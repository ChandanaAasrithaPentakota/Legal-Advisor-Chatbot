from langchain_groq import ChatGroq

import sys
sys.path.append("..")
from config import GROQ_API_KEY #Importing Groq API Key from config.py file

def llm_choice(choice:str):
    """
    Initializes LLM based on user's choice.
    
    Args:
    choice(str): The name of the LLM chosen.
    
    Returns:
    llm: An instance of the ChatGroq class initialized with the selected model and API key.
    """
    if choice.lower()=="deepseek-r1-distill-qwen-32b":
        model="deepseek-r1-distill-qwen-32b"
    elif choice.lower()=="gemma2-9b-it":
        model="gemma2-9b-it"
    else:
        model="llama3-8b-8192"
    llm= ChatGroq(groq_api_key=GROQ_API_KEY,model=model)  
    return llm

