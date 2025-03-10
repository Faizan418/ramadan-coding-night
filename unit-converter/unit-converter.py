import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Unit Converter By Muhammad Faizan", page_icon="🔄", layout="centered")

# Custom CSS for stylish UI
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 45px;
            color: #ffffff;
            font-weight: bold;
            padding-bottom: 10px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
        }
        .box-style {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }
        .stButton > button {
            background: linear-gradient(90deg, #ff416c, #ff4b2b);
            color: white;
            border-radius: 15px;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 15px rgba(255, 65, 108, 0.5);
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #e03e5a, #ff5733);
            transform: scale(1.08);
            box-shadow: 0 6px 20px rgba(255, 65, 108, 0.7);
            color: blue;
        }
        .result-box {
            font-size: 22px;
            color: #155724;
            background: rgba(40, 167, 69, 0.2);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='main-title'>🔄 Unit Converter By Muhammad Faizan...</h1>", unsafe_allow_html=True)

# Function to perform conversions
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not Supported!"

st.markdown("<div class='box-style'>", unsafe_allow_html=True)

# User input fields
value = st.number_input('📏 Enter the value:', min_value=0.0, step=0.1)
unit_from = st.selectbox('🔄 Convert from:', ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox('🔄 Convert to:', ["meters", "kilometers", "grams", "kilograms"])

# Convert button
if st.button('🔁 Convert'):
    result = convert_units(value, unit_from, unit_to)
    st.markdown(f"<div class='result-box'>✅ {value} {unit_from} is equal to {result} {unit_to}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 18px; color: blue;'>✨ Build with ❤️ by [Muhammad Faizan](https://github.com/Faizan418)</p>", unsafe_allow_html=True)
