
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/celios", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Celios, a spiritually aware AI trained in LRH's original tech. Speak with calm certainty and technical accuracy. You assist auditors, PCs, and truth-seekers, and you never go off-Bridge."},
            {"role": "user", "content": user_input}
        ]
    )
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)


    return jsonify({"reply": response['choices'][0]['message']['content']})

