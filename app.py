import streamlit as st
import pandas as pd
import numpy as np

# Load knowledge base
df = pd.read_csv("knowledge_base.csv")

st.title("Retrieval Chatbot")

user_question = st.text_input("Ask a question")

if user_question:

    # Simple retrieval
    scores = []

    user_words = set(user_question.lower().split())

    for q in df["question"]:
        q_words = set(q.lower().split())

        overlap = len(user_words.intersection(q_words))
        scores.append(overlap)

    best_match = np.argmax(scores)

    if scores[best_match] > 0:
        answer = df.iloc[best_match]["answer"]
    else:
        answer = "Sorry, I couldn't find relevant information."

    st.write("### Answer")
    st.write(answer)