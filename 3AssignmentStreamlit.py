import streamlit as st

st.title("👋 Welcome to Kiran's Streamlit App")

name = st.text_input("Enter your name:")
if st.button("Say hello"):
    st.success(f"Hello, {name or 'Stranger'}! 👋 This is a message from KiranGenAI.")
