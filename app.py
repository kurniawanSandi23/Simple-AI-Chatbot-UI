from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API key dari .env
load_dotenv()
api_key = os.getenv("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")  # ← variabel dari .env harus dinamai seperti ini

# Setup OpenAI client
client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("prompt", "")

        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
                max_tokens=1000
            )
            response = completion.choices[0].message.content.strip()

        except Exception as e:
            response = f"Error: {e}"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)