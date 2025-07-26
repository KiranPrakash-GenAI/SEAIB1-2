# SmartCoverLetterWriter.py

import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# --- Load API Key ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Page Setup ---
st.set_page_config(page_title="📄 Smart Cover Letter Writer", layout="centered")
st.title("📄 Smart Professional Cover Letter Writer")
st.markdown("Upload your resume and provide job details to generate a personalized, professional cover letter.")

# --- API Key Check ---
if not api_key:
    st.error("❌ OpenAI API key not found. Please add it to a `.env` file.")
    st.stop()

# --- LangChain Setup ---
llm = ChatOpenAI(api_key=api_key, temperature=0.5, model="gpt-4")

prompt = ChatPromptTemplate.from_template("""
You are an expert career assistant. Using the resume, generate a personalized, professional cover letter for the job below.

## Resume:
{resume}

## Job Title:
{job_title}

## Company:
{company}

## Required Skills:
{skills}

The letter must include:
- A formal greeting
- A strong opening paragraph referencing the job
- A middle section that highlights relevant skills/experience from the resume
- A professional closing
- Keep the tone formal and positive

Output only the cover letter, in plain text.
""")

chain = prompt | llm | StrOutputParser()

# --- Helper: Extract resume text ---
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# --- Input Section ---
with st.form("cover_letter_form"):
    uploaded_resume = st.file_uploader("📎 Upload Your Resume (PDF)", type=["pdf"])
    job_title = st.text_input("💼 Job Title", value="Marketing Analyst")
    company = st.text_input("🏢 Company Name", value="ABC Corp")
    skills = st.text_area("🧠 Required Skills", value="Data analysis, campaign tracking, SEO, presentation skills")

    submitted = st.form_submit_button("✉️ Generate Cover Letter")

# --- Output Section ---
if submitted:
    if not uploaded_resume:
        st.warning("Please upload your resume.")
    elif not job_title or not company:
        st.warning("Please enter both job title and company name.")
    else:
        with st.spinner("Generating your cover letter..."):
            resume_text = extract_text_from_pdf(uploaded_resume)
            output = chain.invoke({
                "resume": resume_text,
                "job_title": job_title,
                "company": company,
                "skills": skills
            })
            st.subheader("✅ Generated Cover Letter")
            st.text_area("📄 Cover Letter", value=output, height=300)

            # Download Option
            st.download_button("⬇️ Download as TXT", output, file_name="CoverLetter.txt")

# --- Footer ---
st.markdown("---")
st.markdown("💼 Crafted with ❤️ by **Kiran Prakash** | Powered by LangChain + OpenAI")
