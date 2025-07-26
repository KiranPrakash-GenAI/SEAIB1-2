import streamlit as st

# Page configuration
st.set_page_config(page_title="📧 Email Username Extractor", layout="centered")

# Title
st.title("📧 Email Username Extractor - Task 19/50")
st.markdown("Enter your email to extract the **username** (part before @).")
st.markdown("App developed by **Kiran Prakash**")

# Input field
email = st.text_input("Enter your email address", placeholder="e.g., name@example.com")

# Button to trigger extraction
if st.button("Extract Username"):
    if email and "@" in email and not email.startswith("@"):
        username = email.split("@")[0]
        st.success(f"✅ **Username extracted:** `{username}`")
    else:
        st.error("❌ Please enter a valid email address.")

# Footer
st.markdown("---")
st.caption("🛠️ Created with ❤️ using Streamlit")
