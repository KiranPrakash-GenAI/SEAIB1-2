import streamlit as st

st.title("🧾 Shopping Bill Generator")

# Buyer name
buyer_name = st.text_input("👤 Enter Buyer's Name")

# Item 1
st.subheader("🛒 Item 1")
item1 = st.text_input("Item 1 Name")
price1 = st.number_input("Item 1 Price", min_value=0.0, format="%.2f")
tax1 = st.number_input("Item 1 Tax (%)", min_value=0.0, max_value=100.0, format="%.2f")

# Item 2
st.subheader("🛒 Item 2")
item2 = st.text_input("Item 2 Name")
price2 = st.number_input("Item 2 Price", min_value=0.0, format="%.2f")
tax2 = st.number_input("Item 2 Tax (%)", min_value=0.0, max_value=100.0, format="%.2f")

# Item 3
st.subheader("🛒 Item 3")
item3 = st.text_input("Item 3 Name")
price3 = st.number_input("Item 3 Price", min_value=0.0, format="%.2f")
tax3 = st.number_input("Item 3 Tax (%)", min_value=0.0, max_value=100.0, format="%.2f")

if st.button("🧾 Generate Bill"):
    # Calculate total per item
    total1 = price1 + (price1 * tax1 / 100)
    total2 = price2 + (price2 * tax2 / 100)
    total3 = price3 + (price3 * tax3 / 100)
    grand_total = total1 + total2 + total3

    st.success("✅ Bill Generated")
    st.write(f"**Buyer:** {buyer_name}")
    st.markdown("---")
    st.write(f"**{item1}**: ₹{price1:.2f} + {tax1}% = ₹{total1:.2f}")
    st.write(f"**{item2}**: ₹{price2:.2f} + {tax2}% = ₹{total2:.2f}")
    st.write(f"**{item3}**: ₹{price3:.2f} + {tax3}% = ₹{total3:.2f}")
    st.markdown("---")
    st.write(f"### 🧮 Total Bill: ₹{grand_total:.2f}")
