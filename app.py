from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the generative model API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the model
def get_gemini_response(question):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)  # Updated function call
        return response.text  # Assuming `response` is a list of generated text items
    

# Initialize Streamlit app layout and configuration
st.set_page_config(page_title="Q&A")

# Display the main header
st.header("🔮 LLM Application") 

# User input and submit button
input = st.text_input("Type your question here:", key="input")
submit = st.button("Submit Question")

# Handle the user's question and model response
if submit:
    response = get_gemini_response(input)
    st.subheader("Response")
    st.write(response)
