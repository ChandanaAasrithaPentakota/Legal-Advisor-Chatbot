# 🧠 Legal Advisor ChatBot using LangChain & Streamlit  

## 🌟 Overview  
This **open-source AI chatbot** is designed to provide **legal guidance** and insights using LangChain and Streamlit, powered by Groq's LLMs for intelligent and context-aware responses. It helps users navigate legal queries, offering general legal information, case law references, and legal document insights while maintaining session-based chat history for a seamless experience.

---

## 🎯 Features  
✔️ **Supports Multiple LLMs** (DeepSeek, Gemma, LLaMA)  
✔️ **Provides real-time legal assistance with conversational AI**  
✔️ **Chat History Preservation** (Session-based memory)  
✔️ **User-friendly Interface** (Built with Streamlit)  
✔️ **Easily Switch Between Models**  
✔️ **Scalable and Customizable**  

---

## 📥 Installation  

### **1️⃣ Clone the Repository**  
```sh  
git clone https://github.com/ChandanaAasrithaPentakota/Legal-Advisor-Chatbot.git  
cd Legal-Advisor-Chatbot  
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**  
```sh  
python -m venv venv  
source venv/bin/activate  # macOS/Linux  
venv\Scripts\activate     # Windows  
```

### **3️⃣ Install Dependencies**  
```sh  
pip install -r requirements.txt  
```

### **🔑 Configuration**  
#### Obtain a Groq API Key  
Get an API key from Groq's official website.  

Create a `config.py` file in the root directory and add your API key:  
```python  
GROQ_API_KEY = "your-api-key-here"  
```

### **🚀 Running the Chatbot**  
```sh  
streamlit run app.py  
```
The app will start on [http://localhost:8501](http://localhost:8501)  
Select a model and start chatting!  

---

## 🏗️ Project Structure  
```bash
Legal-Advisor-Chatbot/
│── assets/
│   ├── demo.png
│── Components/             # Core chatbot components  
│   ├── __init__.py         # Package initialization  
│   ├── chat_history.py     # Handles chat history per session  
│   ├── doc_load_and_process.py  # Loads and processes documents  
│   ├── llm.py              # Language Model (LLM) selection logic  
│   ├── rag_pipeline.py     # Implements Retrieval-Augmented Generation (RAG)  
│── data/                   # Folder for document storage  
│   ├── ConstitutionOfIndia.pdf  # Sample document for processing  
│── LICENSE                 # Open-source license  
│── README.md               # Project documentation  
│── app.py                  # Streamlit UI & main application  
│── config.py               # API key configuration  
│── requirements.txt        # Dependencies
```
---

## 🛠️ How It Works  
🔹 Uses LangChain's Conversational RAG for response generation  
🔹 Maintains chat history per session  
🔹 Dynamically selects LLM based on user preference  
🔹 Streamlit-powered UI for real-time interaction  

---
## 🤝 Contributing  
I welcome feedback and suggestions! 🎉

1️⃣ Fork this repository  
2️⃣ Create a feature branch (`git checkout -b feature-branch`)  
3️⃣ Commit your changes (`git commit -m "Added new feature"`)  
4️⃣ Push the branch (`git push origin feature-branch`)  
5️⃣ Submit a Pull Request  

Your contributions will help improve this chatbot! 🚀  

---

### 📜 Constitution of India - Data Usage & Credits  

The **Constitution of India** document included in this project (`data/ConstitutionOfIndia.pdf`) serves as a sample dataset for document processing, retrieval-augmented generation (RAG), and AI-powered chatbot interactions.  

#### 🏛️ **Source & Attribution**  
This document is publicly available and was downloaded from the official website of the **Legislative Department, Ministry of Law and Justice, Government of India**:  
🔗 [https://legislative.gov.in/constitution-of-india/](https://legislative.gov.in/constitution-of-india/)  

#### ⚖️ **Disclaimer**  
- This document is **freely available** in the public domain as a government publication.  
- The use of this document in this project is solely for **educational, research, and demonstration purposes**.  
- No modifications have been made to the content.  

For authoritative reference or legal use, please visit the official government portal.

---

## ⚖️ License  
This project is open-source under the MIT License.  

Feel free to modify, enhance, or use this project as a base for your own chatbot applications!  

---

## 📩 Contact  
For any suggestions, issues, or feature requests, feel free to open an issue or reach out! 🚀
