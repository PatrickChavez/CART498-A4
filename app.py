# Code from Gabriel Vigliensoni, Google Gemini and OpenAI

import base64
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    generated_image_b64 = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            # --- Text Generation ---
            text_response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system", "content": "You are a psychedelic AI that speaks in Oulipian constraints. Your responses are short, surreal, and witty. Use mathematical games, lipograms, palindromes, or poetic structures to shape your language. Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1.2,
                max_tokens=50
            )
            result = text_response.choices[0].message.content

            # --- Image Generation ---
            image_response = client.images.generate(
                model="gpt-image-1-mini",
                prompt=prompt,
                n=1,
                size="1024x1024"
                # Removed response_format="b64_json" as it seems to be an unknown parameter for gpt-image-1-mini.
                # The model should return b64_json by default if it supports direct base64 output.
            )
            generated_image_b64 = image_response.data[0].b64_json

        except Exception as e:
            result = f"Error generating content: {str(e)}"
            generated_image_b64 = None
            print(f"An error occurred: {e}")

    return render_template("index.html", result=result, generated_image_b64=generated_image_b64)

if __name__ == "__main__":
    app.run(debug=True, port=5000)