# SmartEmailWriter.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# --- Load .env file ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Streamlit config ---
st.set_page_config(page_title="📧 Smart Professional Email Writer", layout="centered")
st.title("📧 Smart Professional Email Writer")
st.markdown("Craft structured and polished emails for business or personal use.")

# --- Error if API key is missing ---
if not api_key:
    st.error("Missing OpenAI API key. Please check your `.env` file.")
    st.stop()

# --- LangChain setup ---
llm = ChatOpenAI(api_key=api_key, temperature=0.4, model="gpt-4")

prompt = ChatPromptTemplate.from_template("""
You are a professional AI email assistant. Given the input details below, craft a clear, polite, and structured email.

Include:
- A subject line
- A formal greeting
- A body in bullet points or paragraphs
- A professional closing

Maintain a respectful, helpful tone.

Details:
Purpose: {purpose}
Recipient: {recipient}
Tone: {tone}
Additional Info: {details}
""")

chain = prompt | llm | StrOutputParser()

# --- UI ---
with st.form("email_form"):
    col1, col2 = st.columns(2)
    with col1:
        recipient = st.text_input("👤 Recipient (e.g., HR Manager)", value="Team Lead")
        tone = st.selectbox("🗣️ Tone", ["Formal", "Polite", "Persuasive", "Apologetic", "Friendly"], index=0)
    with col2:
        purpose = st.text_input("📌 Email Purpose", value="Requesting a project update")

    details = st.text_area("📝 Additional Information", placeholder="Mention specific context, deadlines, attachments, etc.")
    submitted = st.form_submit_button("✉️ Generate Email")

# --- Output ---
if submitted:
    if not purpose or not recipient:
        st.warning("Please provide the required fields: purpose and recipient.")
    else:
        with st.spinner("Generating email..."):
            email = chain.invoke({
                "purpose": purpose,
                "recipient": recipient,
                "tone": tone,
                "details": details
            })

            st.subheader("📨 Generated Email")
            st.code(email, language="markdown")

            st.success("You can copy and paste this into your email client!")

# --- Footer ---
st.markdown("---")
st.markdown("Crafted with ❤️ by **Kiran Prakash** | Powered by LangChain + OpenAI")
