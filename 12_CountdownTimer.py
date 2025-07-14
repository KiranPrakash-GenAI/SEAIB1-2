import streamlit as st
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# --- Page Config ---
st.set_page_config(page_title="⏱️ Countdown Timer", layout="centered")
st.title("⏱️ Countdown Timer with Start, Pause, Lap & Progress")
st.markdown("**Built by Kiran Prakash using Streamlit**")

# --- Refresh every second ---
st_autorefresh(interval=1000, key="refresh")

# --- Session State ---
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "paused" not in st.session_state:
    st.session_state.paused = True
if "elapsed" not in st.session_state:
    st.session_state.elapsed = timedelta()
if "target_duration" not in st.session_state:
    st.session_state.target_duration = timedelta()
if "laps" not in st.session_state:
    st.session_state.laps = []
if "timer_done" not in st.session_state:
    st.session_state.timer_done = False

# --- Time Input ---
st.subheader("🕒 Set Countdown Time")
col1, col2, col3, col4 = st.columns(4)
days = col1.number_input("Days", 0, 30, 0)
hours = col2.number_input("Hours", 0, 23, 0)
minutes = col3.number_input("Minutes", 0, 59, 0)
seconds = col4.number_input("Seconds", 0, 59, 10)

# --- Controls ---
colA, colB, colC, colD = st.columns(4)
if colA.button("▶️ Start"):
    if st.session_state.timer_done:
        st.session_state.elapsed = timedelta()
        st.session_state.laps = []
        st.session_state.timer_done = False
    st.session_state.paused = False
    st.session_state.start_time = datetime.now()
    st.session_state.target_duration = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

if colB.button("⏸️ Pause"):
    st.session_state.paused = True

if colC.button("🔁 Reset"):
    st.session_state.paused = True
    st.session_state.elapsed = timedelta()
    st.session_state.laps = []
    st.session_state.timer_done = False

if colD.button("🏁 Lap"):
    if not st.session_state.paused:
        st.session_state.laps.append(st.session_state.elapsed)

# --- Timer Logic ---
if not st.session_state.paused and not st.session_state.timer_done:
    st.session_state.elapsed += timedelta(seconds=1)

# --- Remaining Time ---
remaining = st.session_state.target_duration - st.session_state.elapsed
if remaining.total_seconds() <= 0 and not st.session_state.timer_done:
    st.session_state.timer_done = True
    st.balloons()
    st.warning("⏰ Time limit reached!")
    remaining = timedelta()

# --- Display Timer ---
st.subheader("⏳ Time Elapsed and Remaining")

colE, colF = st.columns(2)
with colE:
    st.markdown("### 🟢 Elapsed Time")
    st.markdown(f"<h1 style='color: green;'>{str(st.session_state.elapsed).split('.')[0]}</h1>", unsafe_allow_html=True)

with colF:
    st.markdown("### ⏳ Remaining Time")
    st.markdown(f"<h1 style='color: orange;'>{str(remaining).split('.')[0]}</h1>", unsafe_allow_html=True)

# --- Progress Bar ---
if st.session_state.target_duration.total_seconds() > 0:
    progress = min(
        st.session_state.elapsed.total_seconds() / st.session_state.target_duration.total_seconds(), 1.0
    )
    st.progress(progress)

# --- Lap Display ---
if st.session_state.laps:
    st.subheader("🏁 Lap Times")
    for i, lap in enumerate(st.session_state.laps, 1):
        st.markdown(f"- **Lap {i}** — ⏱️ `{str(lap).split('.')[0]}`")
