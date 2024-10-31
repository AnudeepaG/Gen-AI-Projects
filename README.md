<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<img width="871" alt="pic1" src="https://github.com/user-attachments/assets/f50bfa4d-e7d0-48cd-9cef-352fcd0fb214">

<h1>Q&amp;Ask the Oracle</h1>

<img src="https://img.shields.io/badge/Chatbot-Gemini-blue" alt="Chatbot Badge">

<h2>Overview</h2>
<p>
    This project is a Q&amp; A chatbot built using the <strong>Gemini API</strong>. It leverages generative AI capabilities to respond intelligently to user inquiries, creating an interactive and engaging experience. It is developed using <strong>Streamlit</strong>, a popular framework for building data apps in Python.
</p>

<h2>Features</h2>
<ul>
    <li><strong>Natural Language Processing</strong>: Understands and responds to user queries in natural language.</li>
    <li><strong>Interactive Chat Interface</strong>: A user-friendly interface built with Streamlit.</li>
    <li><strong>Dynamic Chat History</strong>: Maintains a conversation history for context-aware responses.</li>
    <li><strong>Customizable Design</strong>: Styled components for a modern and refreshing look.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python</strong>: The primary programming language.</li>
    <li><strong>Streamlit</strong>: For building the web application interface.</li>
    <li><strong>Gemini API</strong>: For generating AI responses.</li>
    <li><strong>HTML/CSS</strong>: For custom styling of the web application.</li>
</ul>

<h3>Install Dependencies</h3>
<p>
    Create a virtual environment (optional but recommended) and install the required packages:
</p>
<pre><code># Create a virtual environment
python -m venv myenv
# To Activate the virtual environment On Windows
myenv\Scripts\activate

# Install dependencies
pip install streamlit
pip install google-generative ai
pip install python-dotenv

</code></pre>

<h3>Set Up Environment Variables</h3>
<p>
    Create a <code>.env</code> file in the root directory of the project and add your Gemini API key:
</p>
<pre><code>GOOGLE_API_KEY=your_api_key_here
</code></pre>

<h2>Running the Application</h2>
<p>
    To start the Streamlit application, run the following command:
</p>
<pre><code>streamlit run qachat.py
</code></pre>
<p>
    This will open your default web browser and navigate to <code>http://localhost:8501</code>, where you can interact with the chatbot.
</p>

<h2>Usage</h2>
<ul>
    <li>Type your question in the input box and click "Submit Question."</li>
    <li>The chatbot will respond with generated answers based on your query.</li>
    <li>The chat history will be displayed below for reference.</li>
</ul>

<h2>Contributing</h2>
<p>
    Contributions are welcome! If you have suggestions for improvements or features, please create a pull request or open an issue.
</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/YourFeature</code>).</li>
    <li>Commit your changes (<code>git commit -m 'Add some feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
    <li>Open a pull request.</li>
</ol>

<h2>License</h2>
<p>
    This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.
</p>

<h2>Acknowledgments</h2>
<ul>
    <li><a href="https://cloud.google.com/generative-ai">Gemini API</a> for providing the powerful AI capabilities.</li>
    <li><a href="https://streamlit.io/">Streamlit</a> for simplifying web app development.</li>
</ul>

</body>
</html>
