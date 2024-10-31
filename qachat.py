from dotenv import load_dotenv
load_dotenv()  # Loading all environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Let's Chat", page_icon="🤖", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
         .main-header {
            font-size: 2.5em;
            color:  #8A8BFF;
            font-weight: 600;
            text-align: center;
            padding: 10px 0;
        }
        .sub-header {
            font-size: 1.5em;
            color: #E6E6FA;
            padding: 5px 0;
        }
        .chat-box {
            background-color: #ECF0F1;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .chat-bubble-user {
            background-color: #AED6F1;
            color: #1A5276;
            padding: 10px;
            border-radius: 8px;
            margin: 5px 0;
            font-weight: bold;
        }
        .chat-bubble-bot {
            background-color: #FAD7A0;
            color: #6E2C00;
            padding: 10px;
            border-radius: 8px;
            margin: 5px 0;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>🔮 Ask the Oracle</div>", unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input box and button with a refreshed look
user_input = st.text_input("Type your question here:", placeholder="What would you like to know?", key="input")
submit = st.button("Submit Question")

# Display response when the button is clicked
if submit and user_input:
    response = get_gemini_response(user_input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", user_input))
    
    st.markdown("<div class='sub-header'>Response:</div>", unsafe_allow_html=True)
    for chunk in response:
        st.markdown(f"<div class='chat-bubble-bot'>{chunk.text}</div>", unsafe_allow_html=True)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history with refreshed style
st.markdown("<div class='sub-header'>Chat History</div>", unsafe_allow_html=True)
for role, text in st.session_state['chat_history']:
    bubble_class = "chat-bubble-user" if role == "You" else "chat-bubble-bot"
    st.markdown(f"<div class='{bubble_class}'>{role}: {text}</div>", unsafe_allow_html=True)
