import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Groq-Powered News Summarizer!"})

@app.route('/summarize-text', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text')
    length = data.get('length', 100)  # Default max tokens

    groq_api_key = os.environ.get('GROQ_API_KEY')  # Ensure this is set

    if not groq_api_key:
        return jsonify({"error": "API key is missing. Set the GROQ_API_KEY environment variable."}), 400

    # Corrected Groq API request
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "compound-beta",  # Use Groq's compound-beta model
        "messages": [{"role": "system", "content": "Summarize the following text"}, {"role": "user", "content": text}],
        "max_tokens": length
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",  # Corrected URL
    headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify(response.json())  # Return summarized text
    else:
        return jsonify({"error": "Groq API error.", "details": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
