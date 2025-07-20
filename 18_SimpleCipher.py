# SimpleCipher.py

import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="🔐 Caesar Cipher Tool", layout="centered")
st.title("🔐 Caesar Cipher Tool")
st.caption("Made with ❤️ by **Kiran Prakash**")

# --- Functions ---
def caesar_cipher(text, shift):
    result = ""
    mapping = []

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            original = char
            shifted = chr((ord(char) - base + shift) % 26 + base)
            mapping.append((original, shifted))
            result += shifted
        else:
            result += char
            mapping.append((char, char))  # unchanged
    return result, mapping

# --- User Inputs ---
st.subheader("🔧 Settings")
col1, col2 = st.columns(2)
mode = col1.radio("Select Mode", ["Cipher", "Decipher"])
shift = col2.slider("Shift Value", min_value=-25, max_value=25, value=1)

if mode == "Decipher":
    shift = -shift

text_input = st.text_area("✍️ Enter your message", height=150)

# --- Output ---
if st.button("🔄 Run Cipher"):
    if text_input.strip() == "":
        st.warning("Please enter some text to continue.")
    else:
        result, mapping = caesar_cipher(text_input, shift)
        st.subheader("🧾 Result")
        st.code(result, language="text")

        # --- Character Mapping ---
        st.subheader("🔠 Character Mapping")
        df_map = pd.DataFrame(mapping, columns=["Original", "Mapped"])
        st.dataframe(df_map.style.highlight_max(axis=0, color="lightgreen"), use_container_width=True)
