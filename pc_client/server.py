from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="OpenAI-api-key")

@app.route("/message", methods=["POST"])
def handle_message():
    data = request.json
    text = data.get("text", "")

    print("收到:", text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个友好的机器人助手。请用简短自然的中文回答。"},
            {"role": "user", "content": text}
        ]
    )

    reply = response.choices[0].message.content
    print("回复:", reply)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)