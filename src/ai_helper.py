import requests
import streamlit as st

API_KEY = st.secrets["OPENROUTER_API_KEY"]

URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openai/gpt-oss-20b"


def ask_ai(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Smart Sales Analytics"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"]