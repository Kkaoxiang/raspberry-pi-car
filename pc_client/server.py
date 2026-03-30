from flask import Flask, request, jsonify
from openai import OpenAI
import pyttsx3
import threading

app = Flask(__name__)
client = OpenAI()

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("语音播放错误:", e)

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

    threading.Thread(target=speak_text, args=(reply,), daemon=True).start()

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)