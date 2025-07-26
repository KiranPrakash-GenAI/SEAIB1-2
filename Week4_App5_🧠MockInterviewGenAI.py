# MockInterviewPrep.py

import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Setup Streamlit
st.set_page_config(page_title="🧠 Mock Interview Generator", layout="centered")
st.title("🧠 Smart Mock Interview Question Generator")
st.markdown("Upload your resume and enter the job profile to generate realistic mock interview questions. Built with LangChain + OpenAI")

# API Key validation
if not api_key:
    st.error("❌ OpenAI API key not found in `.env` file.")
    st.stop()

# LangChain LLM
llm = ChatOpenAI(api_key=api_key, temperature=0.7, model="gpt-4")

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are an expert career coach and interviewer.

Generate a list of professional mock interview questions and sample answers for the job below, using the resume context.

## Resume:
{resume}

## Job Title:
{job_title}

## Key Skills:
{skills}

Format:
- Section 1: Basic HR Questions
- Section 2: Technical Questions (based on job and skills)
- Section 3: Behavioral Questions
- Section 4: Sample Best Answers

Keep tone formal and helpful.
""")

chain = prompt | llm | StrOutputParser()

# Resume Text Extractor
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# --- User Inputs ---
with st.form("interview_form"):
    resume_file = st.file_uploader("📎 Upload Your Resume (PDF)", type=["pdf"])
    job_title = st.text_input("💼 Job Title", value="Data Analyst")
    skills = st.text_area("🧠 Key Skills", value="Python, SQL, Data Visualization, Machine Learning, Statistics")
    submitted = st.form_submit_button("🎯 Generate Mock Interview Questions")

# --- Output Section ---
if submitted:
    if not resume_file:
        st.warning("Please upload a resume PDF.")
    elif not job_title or not skills:
        st.warning("Please provide job title and skills.")
    else:
        with st.spinner("Generating questions..."):
            resume_text = extract_text_from_pdf(resume_file)
            result = chain.invoke({
                "resume": resume_text,
                "job_title": job_title,
                "skills": skills
            })
            st.subheader("📋 Mock Interview Questions")
            st.text_area("📝 Questions & Answers", value=result, height=500)
            st.download_button("⬇️ Download as TXT", result, file_name="MockInterview.txt")

# --- Footer ---
st.markdown("---")
st.markdown("🧠 Created by **Kiran Prakash** | Powered by LangChain + OpenAI")
