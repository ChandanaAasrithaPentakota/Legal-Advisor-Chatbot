from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import streamlit as st

def get_session_history(session_id:str)->BaseChatMessageHistory:
    """
    Creates or retrieves ChatMessageHistory object for a given session_id.
    
    Args:
    session_id(str): A unique Session ID associated with a user session.
    
    Returns:
    BaseChatMessageHistory: The chat history object for a given Session ID
    """
    if session_id not in st.session_state.chat_history:
        st.session_state.chat_history[session_id]=ChatMessageHistory()
    return st.session_state.chat_history[session_id]
    


    