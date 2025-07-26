import streamlit as st
import math

# --- Page Config ---
st.set_page_config(page_title="📐 Area Calculator", layout="centered")

# --- Title ---
st.title("📐 Area Calculator - Task 22/50")
st.markdown("Select a shape and enter the required dimensions to calculate its area.")
st.markdown("App developed by **Kiran Prakash**")

# --- Area Functions ---
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# --- Shape Selection ---
shape = st.selectbox("🔷 Choose a shape:", ["Circle", "Rectangle", "Triangle"])

# --- Input Fields & Calculations ---
if shape == "Circle":
    radius = st.number_input("Enter radius (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_circle(radius)
        st.success(f"🟢 Area of Circle: {area:.2f} cm²")

elif shape == "Rectangle":
    length = st.number_input("Enter length (cm):", min_value=0.0, format="%.2f")
    width = st.number_input("Enter width (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_rectangle(length, width)
        st.success(f"🟢 Area of Rectangle: {area:.2f} cm²")

elif shape == "Triangle":
    base = st.number_input("Enter base (cm):", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_triangle(base, height)
        st.success(f"🟢 Area of Triangle: {area:.2f} cm²")

# --- Footer ---
st.markdown("---")
st.caption("🔢 Made with ❤️ using Streamlit by Kiran Prakash")
