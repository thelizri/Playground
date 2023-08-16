#Detect button press
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    print(GPIO.input(BUTTON_PIN))
    time.sleep(1)

GPIO.cleanup()