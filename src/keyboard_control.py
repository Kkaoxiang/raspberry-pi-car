from src.motor import MotorController


def run_keyboard_control():
    car = MotorController()

    print("Keyboard control started")
    print("w=forward, s=backward, a=left, d=right, x=stop, q=quit")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd == "w":
            car.forward()
        elif cmd == "s":
            car.backward()
        elif cmd == "a":
            car.left()
        elif cmd == "d":
            car.right()
        elif cmd == "x":
            car.stop()
        elif cmd == "q":
            car.stop()
            print("Exit keyboard control")
            break
        else:
            print("Unknown command")