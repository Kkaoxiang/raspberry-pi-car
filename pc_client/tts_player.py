import pyttsx3


class TTSPlayer:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text: str):
        if not text:
            return
        print(f"[TTS] {text}")
        self.engine.say(text)
        self.engine.runAndWait()