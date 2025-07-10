import streamlit as st
import re

# Set Streamlit page config
st.set_page_config(page_title="Password Strength Checker - made by KiranGenAI", page_icon="🔐", layout="centered")

# Title
st.title("🔐 Password Strength Checker - made by KiranGenAI")

# Password Guidelines
with st.expander("📋 Password Requirements"):
    st.markdown("""
    Your password must contain:
    - ✅ At least **8 characters**
    - ✅ At least **one uppercase letter**
    - ✅ At least **one number**
    - ✅ At least **one special character** (`!@#$%^&*()-_+=`)
    """)

# Password Input
password = st.text_input("🔑 Enter your password", type="password")

# Validation Logic
def check_password(pwd):
    length = len(pwd) >= 8
    upper = re.search(r"[A-Z]", pwd)
    digit = re.search(r"\d", pwd)
    special = re.search(r"[!@#$%^&*()\-_=+]", pwd)

    score = sum([length, bool(upper), bool(digit), bool(special)])

    feedback = []
    if not length:
        feedback.append("❌ Minimum length should be 8 characters.")
    if not upper:
        feedback.append("❌ Add at least one **uppercase letter**.")
    if not digit:
        feedback.append("❌ Include at least one **number**.")
    if not special:
        feedback.append("❌ Add a **special character** like `!@#`.")

    return score, feedback

# UI Logic
if password:
    score, issues = check_password(password)

    # Display feedback
    if issues:
        st.error("🔎 Please improve your password:")
        for issue in issues:
            st.write(issue)
    else:
        st.success("✅ Your password meets all requirements!")

    # Strength Indicator
    strength_label = ["Weak", "Medium", "Strong", "Very Strong"]
    strength_color = ["#FF4B4B", "#FACC15", "#22C55E", "#16A34A"]

    st.markdown("### 📊 Password Strength")
    st.progress(score / 4)
    st.markdown(
        f"<div style='color:{strength_color[score-1]}; font-size:24px;'>💪 {strength_label[score-1]}</div>",
        unsafe_allow_html=True
    )
