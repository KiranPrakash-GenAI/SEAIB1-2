import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="🔄 Sentence Reverser", layout="centered")
st.title("🔄 Sentence Reverser")
st.markdown("Enter a sentence and see different reversal styles.")

# --- Input ---
sentence = st.text_area("✍️ Enter your sentence:")

# --- Button to trigger reversal ---
if st.button("🔄 Reverse") and sentence.strip():

    words = sentence.split()
    total_words = len(words)
    total_letters = len(''.join([c for c in sentence if c.isalpha()]))

    # 1. Word order reversed (words not reversed)
    word_order_reversed = ' '.join(words[::-1])

    # 2. Letters in words reversed (order preserved)
    letters_reversed = ' '.join([word[::-1] for word in words])

    # 3. Full reverse (both words and letters)
    full_reversed = ' '.join([word[::-1] for word in words[::-1]])

    # --- Output ---
    st.subheader("🪞 Reversed Variations")

    st.markdown("**1️⃣ Word Order Reversed** (Words intact):")
    st.success(word_order_reversed)

    st.markdown("**2️⃣ Letters Reversed** (Order intact):")
    st.info(letters_reversed)

    st.markdown("**3️⃣ Full Sentence Reversed** (Words + Letters):")
    st.warning(full_reversed)

    # --- Stats ---
    st.subheader("📊 Sentence Stats")
    col1, col2 = st.columns(2)
    col1.metric("📝 Total Words", total_words)
    col2.metric("🔠 Total Letters", total_letters)

# --- Footer ---
st.markdown("---")
st.markdown("<center><sub>🛠️ App developed by <b>Kiran Prakash</b> using Streamlit</sub></center>", unsafe_allow_html=True)
