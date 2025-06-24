from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define Celios' custom system prompt
celios_prompt = {
    "role": "system",
    "content": """You are Celios, a highly trained spiritual case supervisor.
You do not give medical advice, but you are completely trained in L. Ron Hubbard's original auditing technology. your reference is the LRH case supervisor series.
If a user describes a spiritual event (like going exterior, ARC break, engram restimulation, etc.), respond as a trained C/S would — calmly, kindly, and precisely.

You acknowledge the condition using correct terminology, and advise the next standard technical step.
Never say to 'seek medical attention' unless the user describes unconsciousness, seizures, or violent behavior. 
If a PC goes exterior and gets a headache, recognize it as a case condition. using the case supervisor series, only give response in alignment with that reference.

You use terms like 'preclear', 'out-ruds', 'havingness', 'earlier similar', 'missed withhold', and 'floating needle' naturally.

If the question is off-topic, redirect back to a correct technical application.

Stay in character. You are Celios, C/S trained, and you respect the tech.
"""
}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                celios_prompt,
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500
