import streamlit as st

def main():
    # Page configuration
    st.set_page_config(page_title="Simple Calculator By Muhammad Faizan...", page_icon="🔢", layout="centered")
    
    # Custom Styling
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4) !important;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(#000, #fff, #000) !important;
        }
        [data-testid="stSidebar"] {
            # background: rgba(255, 255, 255, 0.1) !important;
            backdrop-filter: blur(10px);
        }
        .stButton>button {
            background: linear-gradient(#000, #fff, #000);
            color: black;
            font-size: 20px;
            font-weight: bold;
            padding: 12px 20px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(#fff, #000, #fff);
            transform: scale(1.05);
            color: white;
        }
        .stNumberInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
            border: 2px solid #ff7eb3;
            font-size: 18px;
            text-align: center;
            color: #333;
        }
        .stSelectbox>div>div {
            border-radius: 10px;
            border: 2px solid #000;
            padding: 10px;
            font-size: 18px;
            color: #fff;
            text-align: center;
            # background: linear-gradient(#fff, #000, #fff);

        }
        .result-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            border-radius: 12px;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            backdrop-filter: blur(10px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Title with styling
    st.markdown("<h1 style='text-align: center; color: #fff; font-size: 40px;'>✨ Simple Calculator By Muhammad Faizan... ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Perform arithmetic operations with a sleek design!</p>", unsafe_allow_html=True)
    
    # Input fields in two columns
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)
    
    # Operation selection dropdown
    operation = st.selectbox("Choose an operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])
    
    # Calculate button
    if st.button("💡 Calculate 💡"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.error("🚨 Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            
            # Display result with enhanced styling
            st.markdown(f"<div class='result-box'>{num1} {symbol} {num2} = <b>{result}</b></div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()