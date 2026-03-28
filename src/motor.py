MOCK_MODE = True

try:
    if not MOCK_MODE:
        from gpiozero import Motor
    else:
        Motor = None
except Exception:
    Motor = None
    MOCK_MODE = True


class MotorController:
    def __init__(self, left_forward=17, left_backward=18, right_forward=22, right_backward=23):
        self.mock = MOCK_MODE or Motor is None
        self.left_motor = None
        self.right_motor = None

        if not self.mock:
            self.left_motor = Motor(forward=left_forward, backward=left_backward)
            self.right_motor = Motor(forward=right_forward, backward=right_backward)

    def _log(self, action: str):
        print(f"[MOTOR] {action}")

    def forward(self):
        if self.mock:
            self._log("forward")
            return
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        if self.mock:
            self._log("backward")
            return
        self.left_motor.backward()
        self.right_motor.backward()

    def left(self):
        if self.mock:
            self._log("left")
            return
        self.left_motor.backward()
        self.right_motor.forward()

    def right(self):
        if self.mock:
            self._log("right")
            return
        self.left_motor.forward()
        self.right_motor.backward()

    def stop(self):
        if self.mock:
            self._log("stop")
            return
        self.left_motor.stop()
        self.right_motor.stop()