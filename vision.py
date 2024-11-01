from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the generative model API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the model
def get_gemini_response(input,image):
        model = genai.GenerativeModel("gemini-1.5-flash")
        if input!="":
            response = model.generate_content([input,image])  
        else:
            response = model.generate_content([input,image])  # Updated function call
        return response.text  # Assuming `response` is a list of generated text items   

# Initialize Streamlit app layout and configuration
st.set_page_config(page_title="Gemini Image Demo")

# Display the main header
st.header("Gemini Application") 

# User input and submit button
input = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)