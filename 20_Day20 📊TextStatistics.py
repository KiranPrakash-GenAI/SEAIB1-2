import streamlit as st
import re

# Page config
st.set_page_config(page_title="📊 Text Statistics", layout="centered")

# Title
st.title("📊 Text Statistics Tool - Task 20/50")
st.markdown("Analyze your paragraph to count **words**, **sentences**, and **characters**.")
st.markdown("App developed by **Kiran Prakash**")

# Input box
text = st.text_area("✍️ Enter your paragraph here:", height=200)

# Button to analyze
if st.button("Analyze Text"):
    if text.strip():
        # Count characters (excluding spaces)
        characters = len(text.replace(" ", ""))

        # Count words
        words = len(re.findall(r'\b\w+\b', text))

        # Count sentences (splitting on common sentence enders)
        sentences = len(re.findall(r'[.!?]+[\s\n]', text)) + (1 if text.strip()[-1] in ".!?" else 0)

        # Display results
        st.subheader("📈 Results:")
        st.write(f"🔠 **Characters (no spaces):** {characters}")
        st.write(f"📝 **Words:** {words}")
        st.write(f"📚 **Sentences:** {sentences}")
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.markdown("---")
st.caption("🛠️ Made with ❤️ using Streamlit by Kiran Prakash")
