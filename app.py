from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load the prompt
try:
    with open("celios_prompt.txt", "r", encoding="utf-8") as f:
        celios_prompt = f.read()
except FileNotFoundError:
    celios_prompt = "You are Celios, an AI trained in spiritual counseling. Use ARC, LRH tech, and always communicate calmly and intelligently."

# Set your OpenAI API key from environment variable (set in Render)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def index():
    return "Celios API is running."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided."}), 400

        messages = [
            {"role": "system", "content": celios_prompt},
            {"role": "user", "content": user_input}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )

        reply = response.choices[0].message["content"]
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
