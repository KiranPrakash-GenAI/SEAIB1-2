# CodingAssistant.py

import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# --- Load environment variables from .env file ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Streamlit Page Config ---
st.set_page_config(page_title="🧑‍💻 GenAI Coding Assistant", layout="wide")
st.title("🧑‍💻 Beginner-Friendly Coding Assistant")
st.markdown("Ask your programming questions and get beginner-friendly help!")

# --- Check API Key ---
if not api_key:
    st.error("API key not found. Please make sure `.env` file contains your `OPENAI_API_KEY`.")
    st.stop()

# --- LangChain Components ---
llm = ChatOpenAI(api_key=api_key, temperature=0.3, model="gpt-4")

prompt = ChatPromptTemplate.from_template("""
You are a helpful and beginner-friendly programming assistant.

Provide a clear and structured answer to the following coding question.
Always include:
1. An easy-to-understand **Explanation**
2. A working **Code Example**
3. The **Expected Output**

Question:
{question}
""")

chain = prompt | llm | StrOutputParser()

# --- UI Input ---
user_question = st.text_area("💬 Ask your coding question:", placeholder="e.g., How to reverse a list in Python?")

if st.button("🚀 Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = chain.invoke({"question": user_question})
            st.markdown("### 🤖 Answer")
            st.markdown(answer)
