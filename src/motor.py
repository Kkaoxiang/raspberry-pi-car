import RPi.GPIO as GPIO
import time

IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def stop():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)

def forward_left():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)

def forward_right():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)

def forward_alternate(duration=2):
    end_time = time.time() + duration

    while time.time() < end_time:
        forward_left()
        time.sleep(0.2)

        forward_right()
        time.sleep(0.2)

    stop()

def cleanup():
    GPIO.cleanup()