# 📊 Smart Sales Analytics & Revenue Prediction System

An AI-powered Business Intelligence Dashboard that combines **Data Analytics, Machine Learning, SQL, and Retrieval-Augmented Generation (RAG)** to analyze business performance, predict future sales, and provide intelligent business recommendations.

> 🚀 Built using Python, Streamlit, Scikit-learn, LangChain, FAISS, Plotly, SQL, and OpenRouter LLM.

---

## 🌐 Live Demo

🔗 **Streamlit App:**  
> https://smart-business-insights.streamlit.app/

---

# 🚀 Features

### 📈 Interactive Dashboard
- KPI Cards (Sales, Profit, Orders)
- Region-wise Sales Analysis
- Category-wise Sales Analysis
- Monthly Sales Trend
- Profit Analysis
- Sales Distribution
- Interactive Filters

---

### 🤖 Machine Learning
- Linear Regression Model
- Sales Prediction
- Model Performance Evaluation
- R² Score
- MAE
- RMSE

---

### 🧠 AI Business Assistant (RAG)

Built using:

- LangChain
- FAISS Vector Database
- Sentence Transformers
- HuggingFace Embeddings
- OpenRouter LLM

The assistant can answer questions like:

- How does discount affect profit?
- Which region performs the best?
- Give business recommendations.
- Which products generate losses?
- Which category has the highest sales?

---

### 📖 AI Prediction Explanation

After every prediction, AI automatically generates:

- 📊 Prediction Summary
- 🔍 Key Factors
- 📈 Business Impact
- 💡 Recommendations
- ✅ Professional Conclusion

---

### 🗄 SQL Analytics

Business Insights include:

- Top Categories by Sales
- Most Profitable Region
- Sales Distribution
- Profit Analysis
- Product Performance

---

# 🛠 Tech Stack

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib
- Streamlit

### Machine Learning
- Scikit-learn
- Joblib

### AI / Generative AI
- LangChain
- FAISS
- HuggingFace Embeddings
- Sentence Transformers
- OpenRouter LLM

### Database
- SQL

---

# 📂 Project Structure

```
Smart-Sales-Analytics-Revenue-Prediction/

│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── documents/
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── app.py
│   ├── rag.py
│   ├── ai_helper.py
│   ├── prepare_documents.py
│   ├── build_vector_db.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```text
Retail Sales Dataset
          │
          ▼
Data Cleaning & Preprocessing
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Machine Learning Model
          │
          ▼
Sales Prediction
          │
          ├──────────────┐
          ▼              ▼
Business Knowledge      Dashboard
          │
          ▼
Sentence Transformers
          │
          ▼
FAISS Vector Database
          │
          ▼
LangChain Retrieval
          │
          ▼
OpenRouter LLM
          │
          ▼
AI Business Assistant
```

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| **R² Score** | **0.91** |
| **MAE** | **₹245.38** |
| **RMSE** | **₹412.56** |

---

# 📷 Dashboard Preview

## 🏠 Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 📊 Sales Prediction

![Sales Prediction](screenshots/sales_prediction.png)
---

## 🤖 AI Business Assistant

![AI Business Assistant](screenshots/ai_business_assistant.png)
---

## 📖 AI Prediction Explanation

![Prediction Explanation](screenshots/prediction_explanation.png)
---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/kbhide47/Smart-Sales-Analytics-Revenue-Prediction.git
```

Move into the project folder

```bash
cd Smart-Sales-Analytics-Revenue-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Build the FAISS Vector Database

```bash
python src/build_vector_db.py
```

Run the Streamlit application

```bash
streamlit run src/app.py
```

---

# 💡 Future Improvements

- Real-time Data Integration
- Time Series Forecasting
- XGBoost & Random Forest Models
- Voice-enabled AI Assistant
- Cloud Deployment (AWS/Azure/GCP)
- Docker Support
- Power BI Integration

---

# 👩‍💻 Author

**Kasturi Anant Bhide**

Electronics & Telecommunication Engineering Student

🎯 Aspiring Data Scientist | AI Engineer | Data Analyst

### GitHub

https://github.com/kbhide47

### LinkedIn

https://www.linkedin.com/in/kasturi-bhide-78334035a/

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and supports future development.

---

## 📬 Contact

For feedback, collaboration, or project discussions, feel free to connect via **GitHub** or **LinkedIn**.






