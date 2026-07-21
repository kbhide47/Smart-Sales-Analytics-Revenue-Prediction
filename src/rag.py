from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from ai_helper import ask_ai

print("Loading Vector Database...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "data/vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Vector Database Loaded")


def ask_rag(question):

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    context += """

The AI Assistant should always answer like a Senior Business Consultant.

Responses should be professional.

Use headings.

Use bullet points.

Explain business impact.

Give practical recommendations.

Avoid mentioning FAISS, LangChain or retrieved documents.

"""

    prompt = f"""
You are a Senior Business Intelligence Consultant with expertise in:

• Sales Analytics
• Revenue Forecasting
• Customer Analytics
• Supply Chain
• Retail Business
• Data Science
• Machine Learning

Use ONLY the retrieved business knowledge below.

Business Knowledge
------------------
{context}

User Question
-------------
{question}

Rules

1. Always answer professionally.

2. Never mention:
   - Vector Database
   - FAISS
   - LangChain
   - Retrieved Documents

3. If information is unavailable, politely say:

"I couldn't find enough business knowledge for this question."

4. Always explain using business language.

5. Whenever possible include:

• Key Findings

• Business Impact

• Recommendation

Return the answer in Markdown.
"""

    return ask_ai(prompt)