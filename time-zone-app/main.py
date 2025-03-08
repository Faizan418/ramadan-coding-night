import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

#........................................ Set page config with icon, title, and wide layout
st.set_page_config(page_title="Time Zone Converter By Muhammad Faizan...", page_icon="⏰", layout="wide")

#........................................ Custom CSS for stylish design
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            color: #ff4500;
            font-weight: bold;
            padding-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #666;
            margin-bottom: 30px;
        }
        .stButton > button {
            background-color: #ff4500;
            color: white;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #cc3700;
            transform: scale(1.05);
        }
        .box-style {
            background: linear-gradient(135deg, #ffffff, #f4f4f4);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .time-display {
            font-size: 18px;
            color: #333;
            padding: 5px;
            border-left: 4px solid #ff4500;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

#........................................ Define available time zones
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo",
    "Australia/Sydney", "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata"
]

#........................................ Title and description
st.markdown("<h1 class='main-title'>🌍 Time Zone Converter By Muhammad Faizan...</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Effortlessly check and convert time across different time zones.</p>", unsafe_allow_html=True)

#........................................ Multi-select dropdown for choosing time zones
st.markdown("<div class='box-style'>", unsafe_allow_html=True)
st.subheader("🕒 Current Time in Selected Timezones")
selected_timezones = st.multiselect("Select Timezones:", TIME_ZONES, default=["UTC", "Asia/Karachi"])
for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.markdown(f"<div class='time-display'>✅ <strong>{tz}</strong>: {current_time}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

#........................................ Time Conversion Section
st.markdown("<div class='box-style'>", unsafe_allow_html=True)
st.subheader("🔄 Convert Time Between Timezones")

#........................................ User input for time selection
current_time = st.time_input("Select Time to Convert:", value=datetime.now().time())
from_tz = st.selectbox("🌍 From Timezone:", TIME_ZONES, index=0)
to_tz = st.selectbox("🌎 To Timezone:", TIME_ZONES, index=1)

#........................................ Convert button with styling
if st.button("🔁 Convert Time", help="Click to convert time to selected timezone"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"**Converted Time in {to_tz}:** `{converted_time}`")

st.markdown("</div>", unsafe_allow_html=True)

#........................................ Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 16px; color: #666;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)