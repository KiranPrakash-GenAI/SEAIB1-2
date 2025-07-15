import streamlit as st
import statistics

# Page Setup
st.set_page_config(page_title="🔢 Number Stats Analyzer", layout="centered")
st.title("📊 Find Largest without Max Fn - Task 13/50")
st.markdown("Enter a list of numbers separated by commas. This app finds the largest number **without using `max()`**, and gives full statistical analysis.")

# Input Field
user_input = st.text_input("🔣 Enter numbers (comma-separated):", placeholder="e.g. 10, 45, -5, 33, 89")

# Function to find the largest manually
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

# Button to process
if st.button("📈 Analyze"):
    try:
        # Convert to list of floats
        num_list = [float(x.strip()) for x in user_input.split(",") if x.strip()]
        
        if not num_list:
            st.warning("⚠️ Please enter some numbers.")
        else:
            # Calculations
            largest = find_largest(num_list)
            average = sum(num_list) / len(num_list)
            mean = statistics.mean(num_list)
            median = statistics.median(num_list)
            try:
                mode = statistics.mode(num_list)
            except statistics.StatisticsError:
                mode = "No unique mode"
            value_range = max(num_list) - min(num_list)

            # Results
            st.subheader("✅ Results")
            st.success(f"🔺 Largest Number (No max()): **{largest}**")
            st.info(f"📉 Average: **{average:.2f}**")
            st.info(f"📊 Mean: **{mean:.2f}**")
            st.info(f"📍 Median: **{median}**")
            st.info(f"🧭 Mode: **{mode}**")
            st.info(f"📐 Range: **{value_range}**")

    except ValueError:
        st.error("❌ Please enter only valid numbers (e.g. 12, 3.5, -4)")

# Footer
st.markdown("---")
st.markdown("<center><sub>🚀 App developed with ❤️ by **Kiran Prakash** using Streamlit</sub></center>", unsafe_allow_html=True)
