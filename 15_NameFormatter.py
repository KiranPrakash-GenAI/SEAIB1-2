import streamlit as st

# Page config
st.set_page_config(page_title="🔠 Name Analyzer", layout="centered")
st.title("🔠 Name Formatter & Numerology Analyzer")
st.markdown("Enter your full name to see different formats and your numerology meaning.")

# Input
full_name = st.text_input("📝 Enter your full name:")

# Meanings of numerology numbers
numerology_meanings = {
    1: "🔢 **1 – Leader**: Independent, ambitious, and innovative.",
    2: "🔢 **2 – Peacemaker**: Diplomatic, sensitive, and cooperative.",
    3: "🔢 **3 – Communicator**: Creative, expressive, and social.",
    4: "🔢 **4 – Builder**: Practical, disciplined, and reliable.",
    5: "🔢 **5 – Explorer**: Adventurous, dynamic, and freedom-loving.",
    6: "🔢 **6 – Nurturer**: Responsible, caring, and protective.",
    7: "🔢 **7 – Thinker**: Analytical, spiritual, and introspective.",
    8: "🔢 **8 – Powerhouse**: Ambitious, efficient, and goal-oriented.",
    9: "🔢 **9 – Humanitarian**: Compassionate, generous, and idealistic.",
    11: "🔮 **11 – Master Intuitive**: Visionary, spiritual, and inspirational.",
    22: "🔮 **22 – Master Builder**: Practical visionary, destined for big achievements.",
    33: "🔮 **33 – Master Teacher**: Compassionate leader, devoted to uplifting others."
}

# Functions
def get_name_formats(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        initials = ''.join([p[0].upper() for p in parts])
        return {
            "First Last": f"{first} {last}",
            "Last, First": f"{last}, {first}",
            "Initials": initials
        }
    else:
        return {
            "Only One Name": name,
            "Initial": name[0].upper()
        }

def get_character_count(name):
    return len(name.replace(" ", ""))

def calculate_numerology(name):
    total = 0
    for char in name.upper():
        if char.isalpha():
            total += ord(char) - 64  # A=1, B=2, ..., Z=26
    # Reduce to single digit (or master number)
    def reduce_number(n):
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
        return n
    return total, reduce_number(total)

# Output
if full_name.strip():
    st.subheader("📂 Name Formats")
    formats = get_name_formats(full_name)
    for k, v in formats.items():
        st.write(f"**{k}**: {v}")

    st.subheader("🔢 Character Analysis")
    count = get_character_count(full_name)
    st.info(f"Total characters (excluding spaces): **{count}**")

    st.subheader("🔮 Numerology")
    total_sum, numerology = calculate_numerology(full_name)
    st.success(f"Numerology Base Sum: **{total_sum}**")
    st.warning(f"Your Core Numerology Number: **{numerology}**")

    meaning = numerology_meanings.get(numerology, "🧐 No meaning found.")
    st.markdown(f"### 📘 Numerology Meaning\n{meaning}")

# Footer
st.markdown("---")
st.markdown("<center><sub>🛠️ App developed by **Kiran Prakash** using Streamlit</sub></center>", unsafe_allow_html=True)

