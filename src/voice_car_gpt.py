import speech_recognition as sr
import requests
import time
from motor import forward_left, forward_right, forward_alternate, stop

PC_URL = "http://192.168.1.213:5000/message"

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

mic = sr.Microphone()

def handle_command(text):
    if "左" in text:
        print("➡️ 左")
        forward_left()
        time.sleep(1)
        stop()

    elif "右" in text:
        print("➡️ 右")
        forward_right()
        time.sleep(1)
        stop()

    elif "前" in text:
        print("⬆️ 前进")
        forward_alternate(2)

    elif "停" in text:
        print("⛔ 停止")
        stop()

    else:
        print("💬 发送给GPT:", text)
        try:
            r = requests.post(PC_URL, json={"text": text}, timeout=10)
            print("已发送:", r.status_code)
        except Exception as e:
            print("发送失败:", e)

while True:
    with mic as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("🧠 Recognizing...")

            text = recognizer.recognize_google(audio, language="zh-CN")
            print("你说的是:", text)

            handle_command(text)

        except sr.UnknownValueError:
            print("❌ 没听清")

        except Exception as e:
            print("❌ 错误:", e)