import streamlit as st

# Set page config
st.set_page_config(page_title="🔡 Name Formatter & Numerology", layout="centered")
st.title("🔡 Name Formatter & Numerology")
st.caption("✨ Built by **Kiran Prakash**")

# Input full name
full_name = st.text_input("Enter your full name:")

# Pythagorean numerology values
numerology_map = {
    'A':1, 'J':1, 'S':1,
    'B':2, 'K':2, 'T':2,
    'C':3, 'L':3, 'U':3,
    'D':4, 'M':4, 'V':4,
    'E':5, 'N':5, 'W':5,
    'F':6, 'O':6, 'X':6,
    'G':7, 'P':7, 'Y':7,
    'H':8, 'Q':8, 'Z':8,
    'I':9, 'R':9
}

# Numerology meanings including master numbers
numerology_meaning = {
    1: "Leader, independent, ambitious.",
    2: "Diplomatic, sensitive, peacemaker.",
    3: "Creative, expressive, joyful.",
    4: "Practical, disciplined, reliable.",
    5: "Adventurous, dynamic, freedom-loving.",
    6: "Nurturing, responsible, loving.",
    7: "Analytical, spiritual, deep thinker.",
    8: "Powerful, ambitious, material success.",
    9: "Compassionate, wise, humanitarian.",
    11: "Intuitive, spiritual messenger, visionary.",
    22: "Master builder, dreams into reality.",
    33: "Compassionate teacher, uplifter of humanity.",
    44: "Master of material and spiritual balance.",
    55: "Freedom-seeker with great influence.",
    66: "Universal nurturer and healer.",
    77: "Sacred wisdom and deep spiritual insight.",
    88: "Master of power and abundance.",
    99: "Ultimate humanitarian, selfless service."
}

# Reduce to single digit unless it's a master number
def reduce_to_single_digit(n):
    while n > 9 and n not in numerology_meaning:
        n = sum(int(d) for d in str(n))
    return n

if full_name.strip():
    # Format display
    st.markdown("### ✨ Initials")
    initials = ''.join([name[0].upper() for name in full_name.split() if name])
    st.markdown(f"<div style='font-size:48px; font-weight:bold; background:black; color:yellow; text-align:center; padding:10px'>{initials}</div>", unsafe_allow_html=True)

    # Name formats
    st.markdown("### 🧾 Name Formats")
    parts = full_name.split()
    first = parts[0] if len(parts) > 0 else ""
    last = parts[-1] if len(parts) > 1 else ""
    middle = ' '.join(parts[1:-1]) if len(parts) > 2 else ""

    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**First Last**: {first} {last}")
        st.info(f"**Last, First**: {last}, {first}")
    with col2:
        st.warning(f"**Initials**: {initials}")
        st.error(f"**Full Name**: {full_name.title()}")

    # Character Count
    total_characters = len(full_name.replace(" ", ""))
    st.markdown(f"### 🔢 Total Characters: **{total_characters}**")

    # Numerology calculation
    total_numerology = sum(numerology_map.get(char.upper(), 0) for char in full_name if char.isalpha())

    # Keep master numbers if available
    if total_numerology in numerology_meaning:
        numerology_number = total_numerology
    else:
        numerology_number = reduce_to_single_digit(total_numerology)

    st.markdown(f"### 🔮 Numerology Number: `{numerology_number}`")
    st.info(f"💡 **Meaning**: {numerology_meaning.get(numerology_number, 'Unknown meaning.')}")
