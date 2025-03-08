import streamlit as st
import random
import time
import requests

# Set page config with icon, title, and wide layout
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")

# Custom CSS for stylish UI
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 40px;
            color: #28a745;
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
            background-color: #28a745;
            color: white;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #218838;
            transform: scale(1.05);
        }
        .box-style {
            background: linear-gradient(135deg, #ffffff, #f4f4f4);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .money-display {
            font-size: 22px;
            color: #155724;
            background-color: #d4edda;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1 class='main-title'>💰 Money Making Machine By Muhammad Faizan</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Generate money, explore side hustles, and get inspired!</p>", unsafe_allow_html=True)

# Money Generator Section
st.markdown("<div class='box-style'>", unsafe_allow_html=True)
st.subheader("💸 Instant Cash Generator")

def generate_money():
    return random.randint(1, 100)

if st.button("💵 Generate Money"):
    st.write("Counting your money...")
    time.sleep(2)
    amount = generate_money()
    st.markdown(f"<div class='money-display'>🎉 You made **${amount}**</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Side Hustle Ideas Section
st.markdown("<div class='box-style'>", unsafe_allow_html=True)
st.subheader("🚀 Side Hustle Ideas")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", "Freelancing")
        else:
            return "Freelancing"
    except:
        return "Something went wrong!"

if st.button("💼 Generate Hustle"):
    idea = fetch_side_hustle()
    st.info(f"💡 {idea}")

st.markdown("</div>", unsafe_allow_html=True)

# Money Motivation Quotes Section
st.markdown("<div class='box-style'>", unsafe_allow_html=True)
st.subheader("📢 Money-Making Motivation")

def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", "Money is the root of all evil")
        else:
            return "Money is the root of all evil"
    except:
        return "Something went wrong!"

if st.button("🔥 Get Inspired"):
    quote = fetch_money_quote()
    st.info(f"📜 {quote}")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 16px; color: #666;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
