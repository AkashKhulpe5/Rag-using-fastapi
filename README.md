##Rag-using-fastapi



## Project Description

A high-performance Retrieval-Augmented Generation (RAG) system utilizing **FastAPI** for a decoupled, asynchronous backend API and **Streamlit** for an intuitive user dashboard. It processes PDF uploads, manages localized semantic search using **FAISS**, and executes ultra-low-latency LLM inference via **Groq**.

---

## README.md

```markdown
# FastAPI & Streamlit RAG Pipeline with Groq

A lightweight, modular Retrieval-Augmented Generation (RAG) application. This project uses a decoupled architecture with an asynchronous FastAPI backend server, a FAISS vector database for lightning-fast localized context retrieval, and a Streamlit frontend UI. High-speed LLM generation is powered by Groq.

## 📁 Project Structure

```text
rag_project/
├── backend/
│   ├── app.py            # FastAPI server & API routing
│   ├── rag.py            # PDF chunking & QA pipeline logic
│   ├── vector_store.py   # FAISS index setup & persistent storage
│   └── uploads/          # Directory for uploaded document storage
├── frontend/
│   └── app.py            # Streamlit user interface
├── .env                  # Environment configurations
└── requirements.txt      # Project dependencies

```

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd rag_project

```

### 2. Configure Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here

```

### 3. Install Dependencies

Ensure you have Python 3.9+ installed, then run:

```bash
pip install -r requirements.txt

```

---

## 🚀 Running the Application

To run the full pipeline, you must spin up both the backend API server and the frontend interface in separate terminal windows.

### Step 1: Start the FastAPI Backend

```bash
python -m uvicorn backend.app:app --reload

```

*The backend server will be live at `http://127.0.0.1:8000` with interactive Swagger docs accessible at `/docs`.*

### Step 2: Start the Streamlit Frontend

```bash
streamlit run frontend/app.py

```
