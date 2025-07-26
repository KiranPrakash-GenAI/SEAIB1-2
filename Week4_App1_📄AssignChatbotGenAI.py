import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load the API key from .env file
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Check that key is loaded
if openai_key is None:
    st.error("❌ OPENAI_API_KEY not found. Please create a .env file.")
    st.stop()

# Initialize LLM
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0)

st.set_page_config(page_title="Simple RAG Chatbot", layout="wide")
st.title("📄 Simple PDF RAG Chatbot")

# File uploader
pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.read())
        pdf_path = tmp_file.name

    # Load and split PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Embed documents
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Setup RAG chain
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    st.success("✅ PDF processed! Ask a question below:")

    # Ask user input
    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa_chain.run(query)
        st.markdown("### 🤖 Answer:")
        st.write(answer)
else:
    st.info("📤 Upload a PDF file to start chatting.")
