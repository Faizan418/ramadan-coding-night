import streamlit as st
import random
import string

# Set page configuration
st.set_page_config(page_title="🔐 Password Generator By Muhammad Faizan", page_icon="🔑", layout="centered")

# Custom CSS for a modern, stylish UI
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
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #eee;
            margin-bottom: 30px;
        }
        .stButton > button {
            background: linear-gradient(90deg, #007bff, #00c6ff);
            color: white;
            border-radius: 15px;
            padding: 12px 30px;
            font-size: 18px;
            border: none;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 15px rgba(0, 123, 255, 0.5);
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #0056b3, #0088cc);
            transform: scale(1.08);
            box-shadow: 0 6px 20px rgba(0, 123, 255, 0.7);
        }
        .password-box {
            font-size: 24px;
            color: #0f5132;
            background: rgba(40, 167, 69, 0.2);
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .box-style {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1 class='main-title'>🔐 Advanced Password Generator By Muhammad Faizan...</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Generate strong and secure passwords instantly!</p>", unsafe_allow_html=True)

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Uppercase and lowercase letters
    if use_digits:
        characters += string.digits  # Add numbers (0-9)
    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&*)
    return "".join(random.choice(characters) for _ in range(length))

# UI layout
st.markdown("<div class='box-style'>", unsafe_allow_html=True)

# Password length selection
length = st.slider("🔢 Select password length:", min_value=6, max_value=32, value=12)

# Checkboxes for password customization
use_digits = st.checkbox("🔢 Include numbers")
use_special = st.checkbox("🔣 Include special characters")

# Button to generate password
if st.button("🔑 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.markdown(f"<div class='password-box'>🔒 Generated Password: `{password}`</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 18px; color: blue;'>✨ Build with ❤️ by [Muhammad Faizan](https://github.com/Faizan418)</p>", unsafe_allow_html=True)
