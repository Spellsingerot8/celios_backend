from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

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
