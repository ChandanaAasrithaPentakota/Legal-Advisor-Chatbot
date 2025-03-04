from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory


def retriever_with_history(llm,retriever):
    """
    Creates a history-aware retriever that reformulates user query, making it standalone.

    Args:
    llm: A language model for reformulating user query.
    retriever: A retriever object that retrieves the most relevant documents for a given query.

    Returns:
    history_aware_retriever: A context-aware retriever object.
    """
    history_aware_system_prompt=("Reframe user questions that refer to past conversation history and"
                "make sure that the question can be understood without chat history."
                "Do not answer the question just reformulate it if necessary. If no" 
                "reformulation is needed, then, return question as is.")
    history_aware_prompt= ChatPromptTemplate.from_messages([
        ("system",history_aware_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human","{input}")
    ])
    history_aware_retriever= create_history_aware_retriever(llm,retriever,history_aware_prompt)
    return history_aware_retriever


def create_document_chain(llm):
    """
    Creates a document chain for answering legal queries based on the Constitution of India.


    Args:
    llm: The language model used to generate responses.

    Returns:
    document_chain: A document chain that takes retrieved documents and generates responses.
    """
    system_prompt= ("You are a legal advisor who helps users answer their questions on legal matters."
            "You have access to the Constitution of India document, which you can use"
            "to answer user questions and give advices, suggestions, etc. Always refer"
            "to the Constitution of India for answers. If you don't know the answer to a"
            "specific user question, just say you don't know. Help the user to the best of"
            "ability, by answering user questions accurately, without any personal opinions."
            "Answer user questions keeping in mind the previous context."
            "\n\n {context}")
    prompt= ChatPromptTemplate.from_messages([
        ("system",system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human","{input}")
    ])
    document_chain= create_stuff_documents_chain(llm,prompt)
    return document_chain

def retrieval_chain(history_aware_retriever,document_chain):
    """
    Creates a Retrieval-Augmented Generation chain by combining a history-aware retriever with a document chain.

    Args:
    history_aware_retriever: A context-aware retriever object that retrieves based on user queries and past conversation history.
    document_chain: A document chain that takes retrieved documents and generates responses.

    Returns:
    rag_chain: A RAG(Retrieval-Augmented Generation) chain.
    """
    rag_chain= create_retrieval_chain(history_aware_retriever,document_chain)
    return rag_chain
    
def create_conversational_rag_chain(rag_chain,get_session_history,input_key="input",chat_history_key="chat_history",output_key="answer"):
    """
    Creates a conversational RAG chain.
    
    Args:
    rag_chain: A RAG(Retrieval-Augmented Generation) chain.
    get_session_history(function): Retrieves conversation history for specified Session ID.
    input_key(str): Key for user input in the message dictionary.
    chat_history_key(str): Key for storing chat history.
    output_key(str): Key for storing model-generated responses.

    Returns:
    conversational_rag_chain: A RAG chain with message history.
    """
    conversational_rag_chain=RunnableWithMessageHistory(rag_chain,
                                                        get_session_history,
                                                        input_messages_key=input_key,
                                                        history_messages_key=chat_history_key,
                                                        output_messages_key=output_key)
    return conversational_rag_chain



