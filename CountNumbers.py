import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Count Numbers - Kiran Prakash", page_icon="🔢", layout="centered")

# Title and Description
st.title("🎯 Count Numbers")
st.markdown("**Developed by: `Kiran Prakash M`**")
st.markdown("This app generates 50 random numbers including **positive**, **negative**, and **zero** values. It then analyzes the count of each type.")

st.markdown("### 🧮 Generated Numbers List")

# Generate random numbers (50 total: -100 to 100)
numbers = [random.randint(-100, 100) for _ in range(50)]

# Display all numbers in a multi-line text box (no scroll)
number_lines = "\n".join(f"{i+1}. {num}" for i, num in enumerate(numbers))
st.text_area("📦 List of 50 Numbers", number_lines, height=300)

# Count statistics
positives = sum(1 for n in numbers if n > 0)
negatives = sum(1 for n in numbers if n < 0)
zeros = numbers.count(0)

# Metrics Section
st.markdown("### 📊 Number Category Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🟢 Positive Numbers", positives)

with col2:
    st.metric("🔴 Negative Numbers", negatives)

with col3:
    st.metric("⚪ Zeros", zeros)

# Final Summary
st.markdown("### 📝 Final Analysis")
summary = f"""
Out of 50 numbers:

- ✅ Positive: **{positives}**
- ❌ Negative: **{negatives}**
- ⚪ Zero: **{zeros}**

All values may repeat. This is a randomly generated dataset.
"""

st.success(summary)

# Footer
st.markdown("---")
st.markdown("<center><sub>🚀 App created with ❤️ by Kiran Prakash using Streamlit</sub></center>", unsafe_allow_html=True)
