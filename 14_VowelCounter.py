import streamlit as st

# Page Configuration
st.set_page_config(page_title="🔤 Vowel Counter", layout="centered")
st.title("🔤 Vowel Counter App")
st.markdown("Enter a word to count how many vowels it has.")

# Input
word = st.text_input("📝 Enter a word", "")

# Function to count vowels
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    breakdown = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    for char in word:
        if char in vowels:
            count += 1
            breakdown[char.upper()] += 1
    return count, breakdown

# Process and display
if word:
    total_vowels, breakdown = count_vowels(word)
    st.success(f"✅ The word **{word}** contains **{total_vowels} vowel(s)**.")
    st.subheader("🔎 Vowel Breakdown")
    st.write(breakdown)

# Footer
st.markdown("---")
st.markdown("<center><sub>🛠️ App developed by **Kiran Prakash** using Streamlit</sub></center>", unsafe_allow_html=True)
