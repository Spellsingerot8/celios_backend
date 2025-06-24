from flask import Flask, request, jsonify
import openaiimport os
from flask import Flask, request, jsonify
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


app = Flask(__name__)

import os
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": data["message"]}
        ]
    )
    return jsonify({"reply": response['choices'][0]['message']['content']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
