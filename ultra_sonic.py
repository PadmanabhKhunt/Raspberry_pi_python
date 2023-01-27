import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 11
GPIO_ECHO = 18

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIG, GPIO.LOW)

time.sleep(2)

GPIO.output(GPIO_TRIG, GPIO.HIGH)

time.sleep(0.00001)

GPIO.output(GPIO_TRIG, GPIO.LOW)

while GPIO.input(GPIO_ECHO) == 0:

    start_time = time.time()
    print (start_time)

while GPIO.input(GPIO_ECHO) == 1:

    Bounce_back_time = time.time()
    print(Bounce_back_time)



pulse_duration = Bounce_back_time - start_time

distance = round(pulse_duration * 17150, 2)

print(f"Distance: {distance} cm")

GPIO.cleanup()

