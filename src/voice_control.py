from src.motor import MotorController


class VoiceController:
    def __init__(self):
        self.car = MotorController()

    def parse_command(self, text: str):
        if not text:
            return None

        text = text.lower()

        if any(word in text for word in ["forward", "go", "ahead", "前进"]):
            return "forward"
        if any(word in text for word in ["back", "backward", "后退"]):
            return "backward"
        if any(word in text for word in ["left", "左"]):
            return "left"
        if any(word in text for word in ["right", "右"]):
            return "right"
        if any(word in text for word in ["stop", "halt", "停"]):
            return "stop"

        return None

    def execute(self, command: str):
        if command == "forward":
            self.car.forward()
        elif command == "backward":
            self.car.backward()
        elif command == "left":
            self.car.left()
        elif command == "right":
            self.car.right()
        else:
            self.car.stop()

    def run_once_from_text(self, text: str):
        command = self.parse_command(text)
        if command is None:
            print("[VOICE] No valid motion command found")
            return None

        self.execute(command)
        print(f"[VOICE] Executed: {command}")
        return command