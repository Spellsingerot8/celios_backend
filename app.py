from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load personality
with open("celios_prompt.txt", "r", encoding="utf-8") as f:
    celios_base = f.read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "I didn't get that."}), 400

    messages = [
        {"role": "system", "content": celios_base},
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.4,
            max_tokens=500
        )
        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"response": "Error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
