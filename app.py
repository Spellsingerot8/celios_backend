import os
import openai
from flask import Flask, request, jsonify

# Initialize OpenAI client using the environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Create Flask app
app = Flask(__name__)

# Define route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json["message"]

        # Call OpenAI ChatCompletion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app if executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
