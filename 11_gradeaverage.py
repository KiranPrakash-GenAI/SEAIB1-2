import streamlit as st
import pandas as pd
import plotly.express as px

# --- App Configuration ---
st.set_page_config(page_title="🎓 Grade Average Analyzer", layout="wide")

# --- Title ---
st.title("🎓 Grade Average Analyzer - Task 11/50")
st.markdown("Analyze performance of **5 students** across **6 subjects**. Includes totals, averages, pass/fail, subject statistics, and visuals.")

# --- Constants ---
NUM_STUDENTS = 5
SUBJECTS = ["Maths", "English", "Science", "Tamil", "Social Science", "Computer"]
PASS_MARK = 40

# --- Input Form ---
students_data = []

with st.form("grade_form"):
    st.header("📝 Enter Student Details")

    for i in range(NUM_STUDENTS):
        st.subheader(f"👤 Student {i+1}")
        col1, col2 = st.columns(2)
        name = col1.text_input(f"Name", key=f"name_{i}")
        student_class = col2.text_input(f"Class", key=f"class_{i}")

        scores = {}
        subject_cols = st.columns(3)
        for j, subject in enumerate(SUBJECTS):
            with subject_cols[j % 3]:
                marks = st.number_input(f"{subject} Marks", min_value=0, max_value=100, key=f"{subject}_{i}")
                scores[subject] = marks

        students_data.append({
            "Name": name,
            "Class": student_class,
            **scores
        })

    submitted = st.form_submit_button("📊 Analyze Results")

# --- On Submit ---
if submitted:
    st.divider()
    df = pd.DataFrame(students_data)

    # Compute Total and Average per student
    df["Total"] = df[SUBJECTS].sum(axis=1)
    df["Average"] = (df["Total"] / len(SUBJECTS)).round(1)

    # Pass/Fail status per subject
    for subject in SUBJECTS:
        df[f"{subject} Status"] = df[subject].apply(lambda x: "✅ Pass" if x >= PASS_MARK else "❌ Fail")

    # Overall pass/fail status
    def overall_status(row):
        failed = sum(1 for subject in SUBJECTS if row[subject] < PASS_MARK)
        return "ALL PASS" if failed == 0 else f"{failed} FAILED"

    df["Overall Status"] = df.apply(overall_status, axis=1)

    # Display Full Table
    st.subheader("📋 Student Performance")
    display_cols = ["Name", "Class", *SUBJECTS, "Total", "Average", "Overall Status"]
    st.dataframe(df[display_cols], use_container_width=True)

    # 🥇 First Rank Holder
    st.subheader("🏆 Top Ranker")
    top_student = df.loc[df["Total"].idxmax()]
    st.success(f"**{top_student['Name']}** from Class {top_student['Class']} scored the highest with **{top_student['Total']}** marks!")

    # 📊 Subject-wise Class Average Table
    st.subheader("📐 Subject-Wise Class Averages")
    subject_avg = df[SUBJECTS].mean().round(1)
    subject_avg_df = pd.DataFrame(subject_avg, columns=["Average Marks"])
    st.table(subject_avg_df)

    # 📈 Subject-wise Class Average Chart
    st.subheader("📊 Visual: Subject Averages Bar Chart")
    chart_df = subject_avg.reset_index()
    chart_df.columns = ["Subject", "Average Marks"]
    fig = px.bar(chart_df, x="Subject", y="Average Marks", color="Average Marks",
                 color_continuous_scale="Aggrnyl", text="Average Marks",
                 labels={"Average Marks": "Avg. Marks"}, height=400)
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("<center><sub>🚀 App created with ❤️ by Kiran Prakash using Streamlit</sub></center>", unsafe_allow_html=True)
