import streamlit as st
import re

# --- Page Config ---
st.set_page_config(page_title="📞 Phone Formatter", layout="centered")

# --- Title ---
st.title("📞 Phone Number Formatter - Task 21/50")
st.markdown("Format any 10-digit number as **(XXX) XXX-XXXX**")
st.markdown("App developed by **Kiran Prakash**")

# --- Input Field ---
phone_input = st.text_input("📲 Enter a 10-digit number:", max_chars=15)

# --- Format Button ---
if st.button("Format Phone Number"):
    digits = re.sub(r'\D', '', phone_input)  # Remove non-digit characters

    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        st.success(f"✅ Formatted Number: `{formatted}`")
    else:
        st.error("❌ Please enter exactly 10 digits.")

# --- Footer ---
st.markdown("---")
st.caption("🛠️ Made with ❤️ using Streamlit by Kiran Prakash")
