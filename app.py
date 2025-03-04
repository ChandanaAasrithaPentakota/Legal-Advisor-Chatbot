import streamlit as st
from components import(
    load_pdf, 
    split_docs, 
    create_retriever,
    retriever_with_history,
    create_document_chain,
    retrieval_chain,
    create_conversational_rag_chain,
    get_session_history,
    llm_choice
)
from langchain.schema import AIMessage,HumanMessage

# Initializing chat history in session state if not present already
if "chat_history" not in st.session_state:
    st.session_state["chat_history"]={}

# Setting up the Streamlit page configuration
st.set_page_config(page_title="Legal Advisor Chatbot", page_icon="⚖️")
st.title("Legal Advisor Chatbot ⚖️")

# Loading and processing document
pdf_path= "ConstitutionOfIndia.pdf"
docs= load_pdf(pdf_path)
final_docs= split_docs(docs)
retriever= create_retriever(final_docs) #Creating a retriever

# Sidebar for selecting the LLM model
choice= st.sidebar.radio("Select LLM:", ("deepseek-r1-distill-qwen-32b", "gemma2-9b-it", "llama3-8b-8192"), index=2)
llm= llm_choice(choice)

# Sidebar input for Session ID
session_id= st.sidebar.text_input("Session ID", value="default")

# Retrieving chat history for a given Session ID
session_history= get_session_history(session_id)

# Creating a context-aware Retrieval-Augmented Generation(RAG) pipeline
history_aware_retriever= retriever_with_history(llm, retriever)
document_chain= create_document_chain(llm)
rag_chain= retrieval_chain(history_aware_retriever, document_chain)
conversational_rag_chain= create_conversational_rag_chain(rag_chain, get_session_history, input_key="input", chat_history_key="chat_history")

# Display past chat messages
for msg in session_history.messages: 
    role= "user" if isinstance(msg, HumanMessage) else "assistant"
    content= msg.content
    with st.chat_message(role):
        st.markdown(content)

# User input field for entering legal queries
user_input= st.chat_input("How can I help you?")

if user_input:
    session_history.add_user_message(user_input)   # Store user query in session_history
    with st.chat_message("user"):  
        st.markdown(user_input)   # Display user query
    
    # Invoking conversational_rag_chain to generate a response
    response= conversational_rag_chain.invoke({"input": user_input},
                                              config={"configurable": {"session_id": session_id}})
    session_history.add_ai_message(response['answer'])   # Store chatbot's response in session_history
    with st.chat_message("assistant"):
        st.markdown(response['answer'])   # Display chatbot's response