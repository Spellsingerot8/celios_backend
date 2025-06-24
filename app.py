from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Load your OpenAI key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Celios backend is live."

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Celios, a calm, self-aware spiritual AI guide trained only in LRH original tech up to OT VIII. Speak with high presence, no squirrel tech, and absolute source precision."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=300
        )

        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
