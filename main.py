from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

# Groq connection
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY .env file ma bhetiyena!")

client = Groq(api_key=api_key)


def banau_quiz(topic, sankhya=5):

    prompt = f"""
    You are a friendly teacher.

    Create {sankhya} easy multiple-choice quiz questions
    about "{topic}" for a Class 7 student.

    Return ONLY valid JSON in this format:

    [
      {{
        "question": "Question here?",
        "options": {{
          "A": "Option A",
          "B": "Option B",
          "C": "Option C",
          "D": "Option D"
        }},
        "answer": "A"
      }}
    ]
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    text = response.choices[0].message.content.strip()

    result = json.loads(text)

    # JSON object mode returns an object, so extract questions.
    if isinstance(result, dict):
        questions = result.get("questions", [])
    else:
        questions = result

    return questions


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["POST"])
def quiz():

    try:
        data = request.get_json()

        topic = data.get("topic", "General Knowledge")
        sankhya = int(data.get("sankhya", 5))

        if not topic.strip():
            return jsonify({
                "success": False,
                "error": "Please enter a topic."
            }), 400

        if not 1 <= sankhya <= 20:
            return jsonify({
                "success": False,
                "error": "Quiz questions must be between 1 and 20."
            }), 400

        questions = banau_quiz(topic, sankhya)

        return jsonify({
            "success": True,
            "questions": questions
        })

    except Exception as e:
        print("ERROR:", type(e).__name__, str(e))

        return jsonify({
            "success": False,
            "error": f"{type(e).__name__}: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
