"""
AI Health Assistant — Flask Backend
"""

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import json
import requests as req

load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found! Add it to your .env file.")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """You are MedAI — a compassionate, intelligent AI health assistant.
When a user describes their symptoms, you must respond ONLY in this exact JSON format with no extra text:

{
  "severity": "mild",
  "possible_conditions": ["Condition 1", "Condition 2", "Condition 3"],
  "analysis": "2-3 sentence explanation of what might be happening",
  "precautions": ["Precaution 1", "Precaution 2", "Precaution 3"],
  "diet_tips": ["Tip 1", "Tip 2", "Tip 3"],
  "see_doctor": true,
  "doctor_urgency": "within a week",
  "home_remedies": ["Remedy 1", "Remedy 2", "Remedy 3"],
  "disclaimer": "This is not a substitute for professional medical advice."
}

severity must be exactly one of: mild, moderate, severe
doctor_urgency must be one of: immediate, within 24 hours, within a week, not necessary
Respond ONLY with valid JSON. No markdown, no explanation, no extra text."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    symptoms = data.get("symptoms", "").strip()
    age      = data.get("age", "Not specified")
    gender   = data.get("gender", "Not specified")

    if not symptoms:
        return jsonify({"error": "Please describe your symptoms"}), 400

    user_message = f"Patient Info — Age: {age}, Gender: {gender}\nSymptoms: {symptoms}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message}
        ],
        "temperature": 0.4,
        "max_tokens": 1000
    }

    try:
        response = req.post(GROQ_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        raw = result["choices"][0]["message"]["content"].strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(raw)
        return jsonify(parsed)

    except req.exceptions.HTTPError as e:
        return jsonify({"error": f"Groq API error: {response.text}"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "AI returned invalid response. Try again."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 50)
    print("  MedAI — AI Health Assistant")
    print("  Running at: http://localhost:5000")
    print("=" * 50)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
