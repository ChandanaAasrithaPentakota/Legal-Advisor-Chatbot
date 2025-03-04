# 🧠 AI ChatBot using LangChain & Streamlit  

## 🌟 Overview  
This is an **open-source AI chatbot** built with **LangChain** and **Streamlit**, utilizing **Groq's LLMs** for intelligent, real-time responses. It supports multiple large language models, maintains session-based chat history, and provides an interactive conversational experience.  

Feel free to modify, improve, or extend this project! 🚀  

---

## 🎯 Features  
✔️ **Supports Multiple LLMs** (DeepSeek, Gemma, LLaMA)  
✔️ **Chat History Preservation** (Session-based memory)  
✔️ **User-friendly Interface** (Built with Streamlit)  
✔️ **Easily Switch Between Models**  
✔️ **Scalable and Customizable**  

---

## 📥 Installation  

### **1️⃣ Clone the Repository**  
```sh  
git clone https://github.com/your-username/AI-ChatBot.git  
cd AI-ChatBot  
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
AI-ChatBot/  
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

---

## 🛠️ How It Works  
🔹 Uses LangChain's Conversational RAG for response generation  
🔹 Maintains chat history per session  
🔹 Dynamically selects LLM based on user preference  
🔹 Streamlit-powered UI for real-time interaction  

---

## 🤝 Contributing  
We welcome contributions! 🎉  

1️⃣ Fork this repository  
2️⃣ Create a feature branch (`git checkout -b feature-branch`)  
3️⃣ Commit your changes (`git commit -m "Added new feature"`)  
4️⃣ Push the branch (`git push origin feature-branch`)  
5️⃣ Submit a Pull Request  

Your contributions will help improve this chatbot! 🚀  

---

## ⚖️ License  
This project is open-source under the MIT License.  

Feel free to modify, enhance, or use this project as a base for your own chatbot applications!  

---

## 📩 Contact  
For any suggestions, issues, or feature requests, feel free to open an issue or reach out! 🚀  
