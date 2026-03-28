import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_once(self, timeout=5, phrase_time_limit=5):
        with sr.Microphone() as source:
            print("[STT] Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[STT] Listening...")

            audio = self.recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"[STT] Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("[STT] Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"[STT] Request error: {e}")
            return None