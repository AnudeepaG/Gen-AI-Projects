<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<img width="871" alt="pic1" src="https://github.com/user-attachments/assets/f50bfa4d-e7d0-48cd-9cef-352fcd0fb214">
<h1>Ask the Oracle</h1>
<img src="https://img.shields.io/badge/Chatbot-Gemini-blue" alt="Chatbot Badge">
<h2>Overview</h2>
<p>
    A chatbot built using the <strong>Gemini API</strong>. It leverages generative AI capabilities to respond intelligently to user enquiries, creating an interactive and engaging experience. Developed using <strong>Streamlit</strong>, a popular framework for building data apps in Python.
</p>

<h2>Features</h2>
<ul>
    <li><strong>Natural Language Processing</strong>: Understands and responds to user queries in natural language.</li>
    <li><strong>Interactive Chat Interface</strong>: User-friendly interface built with Streamlit.</li>
    <li><strong>Dynamic Chat History</strong>: Maintains conversation history for context-aware responses.</li>
    <li><strong>Customizable Design</strong>: Styled components for a modern and refreshing look.</li>
</ul>

<h3>Install Dependencies</h3>
<p>
    Create a virtual environment and install required packages:
</p>
<pre><code>
python -m venv myenv
# To Activate virtual environment On Windows
myenv\Scripts\activate

# Install dependencies
pip install streamlit
pip install google-generative ai
pip install python-dotenv

</code></pre>
<h3>Set Up Environment Variables</h3>
<p>
    Create a <code>.env</code> file in root directory of project and add your Gemini API key:
</p>
<pre><code>GOOGLE_API_KEY=your_api_key_here
</code></pre>

<h2>Running the Application</h2>
<pre><code>streamlit run qachat.py
</code></pre>
<p>
    This will open your default web browser and navigate to <code>http://localhost:8501</code>, where you can interact with the chatbot.
</p>
