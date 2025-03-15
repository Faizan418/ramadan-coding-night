import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why did the programmer quit his job?\nBecause he didn't get array!"

def main():
    """Main function to run the Streamlit app"""
    st.set_page_config(page_title="Random Joke Generator", page_icon="😂", layout="centered")
    
    # Custom CSS for colorful gradient background and stylish UI
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(to top, #fff, #000, #fff);
                color: white;
                font-family: Arial, sans-serif;
            }
            .title {
                text-align: center;
                font-size: 2.5rem;
                font-weight: bold;
                color: #fff;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
            .joke-box {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                font-size: 1.2rem;
                text-align: center;
                color: #fff;
                margin-top: 20px;
            }
            .footer {
                text-align: center;
                font-size: 0.9rem;
                margin-top: 50px;
                color: #fff;
            }
            .stButton>button {
                background: linear-gradient(to top, #fff, #000, #fff);
                color: white;
                font-size: 1rem;
                border-radius: 10px;
                padding: 10px 20px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                transition: 0.3s;
            }
            .stButton>button:hover {
                background: linear-gradient(to top, #000, #fff, #000);
                transform: scale(1.05);
                color: #000;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<div class='title'>😂 Random Joke Generator 😂</div>", unsafe_allow_html=True)
    st.write("### Click the button below to get a hilarious joke! 🤣")
    
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='footer'>
            <p>Joke from Official Joke API</p>
            <p>Built with ❤️ by <a href='https://github.com/Faizan418' target='_blank' style='color: white;'>Muhammad Faizan</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()