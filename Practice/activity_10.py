# import os
# import time
# from picamera import PiCamera

# FOLDER_NAME = "/home/pi/activity_10"

# if not os.path.exists(FOLDER_NAME):
#     os.mkdir(FOLDER_NAME)

# camera = PiCamera()
# camera.resolution = (1280, 720)
# camera.rotation = 180
# time.sleep(2)

# counter = 1

# while True:
#     file_name = FOLDER_NAME + "/img" + str(counter) + ".jpg"
#     counter += 1
#     camera.capture(file_name)
#     print("New photo has been taken")
#     time.sleep(5)


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO_BUZZ = 12
GPIO_TRIG = 24
GPIO_ECHO = 23

GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
# GPIO.setup(GPIO_BUZZ, GPIO.OUT)

# buzzer = GPIO.PWM(GPIO_BUZZ, 50)
# buzzer.start(0)
while (1):

    GPIO.output(GPIO_TRIG, GPIO.LOW)

    time.sleep(0.5)
    GPIO.output(GPIO_TRIG, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(GPIO_TRIG, GPIO.LOW)

    while GPIO.input(GPIO_ECHO) == 0:

        start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:

        Bounce_back_time = time.time()

    pulse_duration = Bounce_back_time - start_time

    distance = round(pulse_duration * 17150, 2)

    print("distance :" + str(distance) + "cm")

    # for distance in range(0, 101, 1):
    #     buzzer.ChangeDutyCycle(distance)
    #     time.sleep(0.1)
    # for distance in range(100, -1, -1):
    #     buzzer.ChangeDutyCycle(distance)
    #     time.sleep(0.1)


GPIO.cleanup()
