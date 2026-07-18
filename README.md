# 📊 Smart Sales Analytics & AI Revenue Prediction Platform

An end-to-end **AI-powered Sales Analytics Platform** built using **Python, SQL, Machine Learning, Streamlit, LangChain, FAISS, Hugging Face Embeddings, and OpenRouter**.

The application enables businesses to analyze sales performance, predict future revenue using Machine Learning, and interact with their sales data through an intelligent Retrieval-Augmented Generation (RAG) chatbot.

---

# 🚀 Project Overview

This project combines **Business Intelligence**, **Machine Learning**, and **Generative AI** into one platform.

Users can:

- Analyze historical sales data
- Visualize KPIs and business trends
- Predict future sales
- Ask business questions using an AI chatbot
- Receive AI-generated business recommendations
- Understand prediction reasoning with Explainable AI

---

# ✨ Features

## 📈 Interactive Dashboard

- KPI Cards
- Region-wise Sales
- Category-wise Sales
- Profit Analysis
- Interactive Plotly Charts
- Dashboard Filters

---

## 🤖 AI Business Assistant (RAG)

- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- LangChain Retrieval Pipeline
- Hugging Face Embeddings
- OpenRouter LLM
- Chat History
- Business Knowledge Search
- Displays Retrieved Knowledge Sources

Example Questions:

- Which region has the highest sales?
- Which category generated the highest profit?
- Suggest ways to improve profit.
- Which customer segment performs best?

---

## 💰 Machine Learning

- Sales Prediction Model
- One-Hot Encoding
- Linear Regression
- Explain Prediction Feature
- AI-generated Recommendation after Prediction

---

## 💡 AI Recommendation Engine

Automatically generates recommendations such as:

- Improve inventory allocation
- Reduce unnecessary discounts
- Focus marketing on profitable regions
- Increase sales in high-performing categories

---

# 🛠 Tech Stack

## Programming

- Python

## Database

- SQLite
- SQL

## Machine Learning

- Scikit-learn
- NumPy
- Pandas

## Data Visualization

- Plotly
- Streamlit

## AI / LLM

- LangChain
- FAISS
- Hugging Face Embeddings
- Sentence Transformers
- OpenRouter API

---

# 📂 Folder Structure

```text
PROJECT_Smart-Sales-Analytics-Revenue-Prediction
│
├── assets/
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── documents/
│   └── vectorstore/
│
├── images/
├── models/
│   ├── best_model.pkl
│   └── onehot_encoder.pkl
│
├── sql/
├── src/
│   ├── app.py
│   ├── ai_helper.py
│   ├── rag.py
│   ├── build_vector_db.py
│   ├── prepare_documents.py
│   ├── model.py
│   ├── eda.py
│   ├── cleaning.py
│   ├── database.py
│   └── data_loading.py
│
├── create_database.py
├── requirements.txt
├── README.md
└── superstore.db
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
```

Move into the project

```bash
cd PROJECT_Smart-Sales-Analytics-Revenue-Prediction
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create the vector database

```bash
python src/build_vector_db.py
```

Run the application

```bash
streamlit run src/app.py
```

---

# 📷 Screenshots

## Dashboard

_Add dashboard screenshot here_

---

## Sales Prediction

_Add prediction screenshot here_

---

## AI Business Assistant

_Add chatbot screenshot here_

---

## AI Recommendation

_Add recommendation screenshot here_

---

# 🔥 Example AI Questions

```
Which region has the highest sales?

Which category generated the highest profit?

Suggest strategies to improve revenue.

How can profit be increased?

Which customer segment contributes the most sales?
```

---

# 📊 Machine Learning Workflow

```
Raw Dataset

↓

Data Cleaning

↓

EDA

↓

Feature Engineering

↓

Model Training

↓

Sales Prediction

↓

Explain Prediction

↓

AI Recommendation
```

---

# 🤖 RAG Workflow

```
Business Knowledge

↓

Document Loader

↓

Text Splitter

↓

Sentence Transformers

↓

FAISS Vector Database

↓

LangChain Retriever

↓

OpenRouter LLM

↓

Business Answer
```

---

# 📌 Future Improvements

- Deploy on Streamlit Cloud
- Authentication System
- Voice-enabled AI Assistant
- Sales Forecasting using Time Series Models
- PDF Report Generation
- Multi-language Support
- Real-time Database Integration
- Interactive Executive Dashboard

---

# 👩‍💻 Developer

**Kasturi Bhide**

Electronics & Telecommunication Engineering

Python | SQL | Machine Learning | Data Analytics | Generative AI | RAG

---

# ⭐ If you found this project useful, consider giving it a Star.


