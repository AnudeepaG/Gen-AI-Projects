from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the generative model API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to initialize the chat with the Gemini model
def initialize_chat():
    model = genai.GenerativeModel("gemini-pro")
    return model.start_chat(history=[])

# Function to get a response from the model
def get_gemini_response(chat, question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app layout and configuration
st.set_page_config(page_title="Let's Chat", page_icon="🤖", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main-header { font-size: 2.5em; color: #8A8BFF; font-weight: 600; text-align: center; padding: 10px 0; }
        .sub-header { font-size: 1.5em; color: #E6E6FA; padding: 5px 0; }
        .chat-box { background-color: #ECF0F1; padding: 15px; border-radius: 10px; margin: 10px 0; }
        .chat-bubble-user { background-color: #AED6F1; color: #1A5276; padding: 10px; border-radius: 8px; margin: 5px 0; font-weight: bold; }
        .chat-bubble-bot { background-color: #FAD7A0; color: #6E2C00; padding: 10px; border-radius: 8px; margin: 5px 0; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Display the main header
st.markdown("<div class='main-header'>🔮 Ask the Oracle</div>", unsafe_allow_html=True)

# Initialize the chat object and session state for chat history if they don't exist
if 'chat' not in st.session_state:
    st.session_state['chat'] = initialize_chat()
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input and submit button
user_input = st.text_input("Type your question here:", placeholder="What would you like to know?", key="input")
submit = st.button("Submit Question")

# Handle the user's question and model response
if submit and user_input:
    response = get_gemini_response(st.session_state['chat'], user_input)
    
    # Add user query and bot response to chat history
    st.session_state['chat_history'].append(("You", user_input))
    
    st.markdown("<div class='sub-header'>Response:</div>", unsafe_allow_html=True)
    for chunk in response:
        st.markdown(f"<div class='chat-bubble-bot'>{chunk.text}</div>", unsafe_allow_html=True)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.markdown("<div class='sub-header'>Chat History</div>", unsafe_allow_html=True)
for role, text in st.session_state['chat_history']:
    bubble_class = "chat-bubble-user" if role == "You" else "chat-bubble-bot"
    st.markdown(f"<div class='{bubble_class}'>{role}: {text}</div>", unsafe_allow_html=True)
