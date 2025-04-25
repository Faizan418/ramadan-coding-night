import subprocess
import streamlit as st
import pandas as pd
import time
import random

# Custom CSS for ultra khataarnaak hacker UI
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background: #000;
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
    
    /* Title styling */
    h1 {
        color: #00ff00;
        text-align: center;
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
        animation: glitch 0.8s linear infinite;
    }
    
    /* Glitch animation */
    @keyframes glitch {
        2%, 64% { transform: translate(3px, 0) skew(2deg); }
        4%, 60% { transform: translate(-3px, 0) skew(-2deg); }
        62% { transform: translate(0, 0) skew(8deg); }
    }
    
    /* Button styling with glitch */
    .stButton>button {
        background: #00ff00;
        color: #000;
        border: 2px solid #00ff00;
        border-radius: 5px;
        padding: 12px 24px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-transform: uppercase;
        box-shadow: 0 0 15px #00ff00;
        transition: all 0.3s ease;
        animation: button-glitch 2s linear infinite;
    }
    .stButton>button:hover {
        background: #000;
        color: #00ff00;
        box-shadow: 0 0 25px #00ff00;
    }
    @keyframes button-glitch {
        0% { transform: translate(0, 0); }
        2% { transform: translate(2px, -1px); }
        4% { transform: translate(-2px, 1px); }
        6% { transform: translate(0, 0); }
    }
    
    /* Table styling with subtle glitch */
    .stTable table {
        background: #111;
        color: #00ff00;
        border: 2px solid #00ff00;
        border-radius: 5px;
        animation: table-glitch 3s linear infinite;
    }
    .stTable th {
        background: #00ff00;
        color: #000;
        text-transform: uppercase;
    }
    .stTable td {
        border-bottom: 1px solid #00ff00;
    }
    @keyframes table-glitch {
        0% { transform: translate(0, 0); }
        3% { transform: translate(1px, 0); }
        6% { transform: translate(-1px, 0); }
        9% { transform: translate(0, 0); }
    }
    
    /* Success, error, and warning messages */
    .stSuccess, .stError, .stWarning {
        background: #111;
        color: #00ff00;
        border: 2px solid #00ff00;
        border-radius: 5px;
        padding: 10px;
        font-family: 'Courier New', monospace;
    }
    
    /* Digital rain background */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3FhcG9tcHl0N2x3c3J2N2Y3YzZ0bDJzYzU4d3Y2N3F3c2hrcXVuNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btPCcdNniyf0ArS/giphy.gif') repeat;
        opacity: 0.3;
        z-index: -1;
    }
    
    /* ASCII art and quotes */
    .ascii-art {
        color: #00ff00;
        text-align: center;
        font-size: 14px;
        line-height: 1.2;
    }
</style>
""", unsafe_allow_html=True)

# ASCII art for hacker vibe
ASCII_ART = """
   _____ _          _ _       
  |  ___| |__   ___| | | ___  
  | |_  | '_ \ / __| | |/ _ \ 
  |  _| | | | | (__| | | (_) |
  |_|   |_| |_| \___|_|_|\___/
       WiFi Credential Extractor
"""

# Random hacker quotes
HACKER_QUOTES = [
    "We're in! System compromised!",
    "Access granted. You're welcome.",
    "Hacked the mainframe. Easy.",
    "Credentials exposed. Stay sharp!",
    "Matrix breached. Who's next?"
]

def get_wifi_passwords():
    try:
        # Step 1: Get list of all WiFi profiles
        command = "netsh wlan show profiles"
        result = subprocess.check_output(command, shell=True, text=True)
        
        # Extract profile names
        profiles = [line.split(":")[1].strip() for line in result.splitlines() 
                    if "All User Profile" in line]
        
        wifi_data = []
        # Step 2: Get password for each profile
        for profile in profiles:
            try:
                # Run command to get details of the specific profile
                command = f'netsh wlan show profile name="{profile}" key=clear'
                profile_info = subprocess.check_output(command, shell=True, text=True)
                
                # Extract password
                for line in profile_info.splitlines():
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        wifi_data.append({"WiFi Name": profile, "Password": password})
                        break
                else:
                    wifi_data.append({"WiFi Name": profile, "Password": "Not found or open network"})
                    
            except subprocess.CalledProcessError:
                wifi_data.append({"WiFi Name": profile, "Password": "Error: Unable to retrieve password"})
                
        return wifi_data, None
    
    except subprocess.CalledProcessError:
        return None, "Error: Unable to fetch WiFi profiles. Run the script as Administrator."
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

def fake_hacking_animation():
    # More intense hacking messages
    messages = [
        "Booting quantum decryptor...",
        "Scanning 2.4GHz/5GHz bands...",
        "Cracking AES-256 encryption...",
        "Spoofing MAC address...",
        "Capturing WPA2 handshake...",
        "Brute-forcing keychain...",
        "Credentials decrypted!"
    ]
    
    placeholder = st.empty()
    for msg in messages:
        # Simulate typing effect
        current_text = ""
        for char in msg:
            current_text += char
            placeholder.markdown(f"```bash\n{current_text}\n```")
            time.sleep(random.uniform(0.03, 0.08))  # Fast typing effect
        time.sleep(random.uniform(0.5, 1.0))  # Pause between messages
    placeholder.empty()

def main():
    # ASCII art logo
    st.markdown(f"<pre class='ascii-art'>{ASCII_ART}</pre>", unsafe_allow_html=True)
    
    # App title with hacker vibe
    st.title("💾 WiFi Credential Extractor")
    st.markdown("`> Breach the network. Extract credentials like a pro.`", unsafe_allow_html=True)
    
    # Add beep sound on button click (browser-based)
    st.markdown("""
    <audio id="beep" src="https://www.soundjay.com/buttons/beep-01a.mp3"></audio>
    <script>
        document.querySelector('.stButton>button').addEventListener('click', function() {
            document.getElementById('beep').play();
        });
    </script>
    """, unsafe_allow_html=True)
    
    # Start hack button
    if st.button(">> Hack WiFi Passwords"):
        # Run fake hacking animation
        fake_hacking_animation()
        
        with st.spinner("> Infiltrating network..."):
            wifi_data, error = get_wifi_passwords()
            
            if error:
                st.error(f"> [ERROR] {error}")
            else:
                if wifi_data:
                    st.success("> [SUCCESS] Credentials extracted!")
                    # Convert to DataFrame for table display
                    df = pd.DataFrame(wifi_data)
                    st.table(df)
                    # Show random hacker quote
                    st.markdown(f"> `{random.choice(HACKER_QUOTES)}`", unsafe_allow_html=True)
                else:
                    st.warning("> [WARNING] No WiFi profiles detected.")
    
    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #00ff00;'>[SYSTEM] Powered by Streamlit | Elite Hacking Interface v1.0 Created By Muhammad Faizan...</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()