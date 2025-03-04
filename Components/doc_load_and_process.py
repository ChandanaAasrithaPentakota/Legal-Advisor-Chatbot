from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import sys
sys.path.append("..") 
from config import HF_TOKEN  #Importing Hugging Face token from config.py file

def load_pdf(pdf_path):
    """
    Loads a PDF and extracts its content.
    
    Args:
    pdf_path(str): The path to the PDF to be loaded.
    
    Returns:
    docs(list): A list of extracted document objects from the PDF.
    """
    loader=PyPDFLoader(pdf_path)
    docs=loader.load()
    return docs 

def split_docs(docs):
    """
    Splits the documents into text chunks.

    Args:
    docs(list): A list of document objects to be split into text chunks.
    
    Returns:
    final_docs(list): A list of split document objects.
    """
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    final_docs=splitter.split_documents(docs)
    return final_docs

def create_retriever(final_docs):
    """
    Creates a Retriever.

    Args:
    final_docs(list): A list of document objects to be embedded and stored.
    
    Returns:
    retriever: A retriever object that retrieves the most relevant documents for a given query.
    """
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorstore=Chroma.from_documents(documents=final_docs,embedding=embeddings,persist_directory="./chroma_db")
    retriever=vectorstore.as_retriever()
    return retriever

if __name__ == "__main__":
    docs=load_pdf('ConstitutionOfIndia.pdf')  #Example usage for load_pdf function
    print(docs)
    final_docs=split_docs(docs)  #Example usage for split_docs function
    print(final_docs)
    vectorstore=create_retrifromever(final_docs)  #Example usage for create_retriever function
    print(vectorstore)
