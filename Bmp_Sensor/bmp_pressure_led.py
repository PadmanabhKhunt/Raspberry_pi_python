import Motion_Detection_Photo_Capturing.Bmp_Sensor.bmpsensor as bmpsensor
import RPi.GPIO as GPIO
import time
LED_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    time.sleep(0.01)
    temp, pressure, altitude = bmpsensor.readBmp180()
    if temp > 25:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_PIN, GPIO.LOW)
    elif (temp < 25):
        GPIO.output(LED_PIN, GPIO.LOW)
        
    print("Temperature is ",temp)  # degC
    print("Pressure is ",pressure) # Pressure in Pa 
    print("Altitude is ",altitude) # Altitude in meters
    print("\n")
    time.sleep(2)
    
GPIO.cleanup() 
