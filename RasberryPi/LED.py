import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
for i in range(5):
	GPIO.output(LED_PIN, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(LED_PIN, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()