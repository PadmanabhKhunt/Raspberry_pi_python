import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os
import yagmail

def take_photo(camera):
    filename = "/home/pi/Desktop/image" + str(time.time()) + ".jpg"
    camera.capture(filename)
    return filename\

def update_photo(photo_file_name):
    with open(LOG_FILE_NAME, 'a') as f:
        f.write(photo_file_name)
        f.write('\n')

def send_email(yagmail_client,file_name):
    yagmail_client.send(to="ankitganatra@gmail.com",
                        subject="Movement Detected",
                        contents="SECURITY ALERT",
                        attachments=file_name)
    



PIR_PIN=4
LED_PIN=18
LOG_FILE_NAME= "/home/pi/Desktop/photo_log.txt"

camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
print("wait 2 second")
time.sleep(2)
print("camara is set")

if os.path.exists(LOG_FILE_NAME):
    os.remove(LOG_FILE_NAME)
    print("Log file is removed")

password =""
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()
yag =yagmail.SMTP("padmanabhkhunt@gmail.com", password)  
print("Email setup done")


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
print("GPIOs is set")

last_pir_state = GPIO.input(PIR_PIN)
movemene_timer= time.time()
MOW_DETECT_TRESHOLD = 3.0
last_time_photo_taken = 0
Photo_Duration = 60.0



try:
    while True:
        time.sleep(0.01)
        pir_state=GPIO.input(PIR_PIN)
        if pir_state == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        if last_pir_state==GPIO.LOW and pir_state==GPIO.HIGH:
            movemene_timer = time.time()
        if last_pir_state==GPIO.HIGH and pir_state==GPIO.HIGH:
            if time.time() - movemene_timer > MOW_DETECT_TRESHOLD:
                if time.time() - last_time_photo_taken > Photo_Duration:
                    photo_file_name =take_photo(camera)
                    update_photo(photo_file_name)
                    send_email(yag ,photo_file_name)
                    last_time_photo_taken = time.time()
            last_pir_state = pir_state
except KeyboardInterrupt:
    GPIO.cleanup()




