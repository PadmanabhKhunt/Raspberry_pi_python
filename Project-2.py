import os
from flask import Flask
import os

CAMARA_FOLDER_PATH="/home/pi/Desktop/camera"
LOG_FILE_NAME= "/home/pi/Desktop/photo_log.txt"
photo_counter=0

app = Flask(__name__,static_url_path='CAMARA_FOLDER_PATH')

@app.route('/')
def index():
    return "hello padmanabh" 

@app.route('/check-movement')
def check_movement():
    massage=""
    line_counter=0
    if os.path.exists(LOG_FILE_NAME):
        with open(LOG_FILE_NAME, "r") as f:
            for line in f:
                line_counter+=1
                last_photo_file_name = line
        global photo_counter        
        difference= line_counter - photo_counter        
        massage=str(difference)+ "photos were thken since you last checked. </br></br> "
        massage+= "last photo:" + last_photo_file_name
        massage+="<img= src=\"" + last_photo_file_name + "\" >"
        photo_counter=line_counter
    else:
        massage="No movement"
    return massage

        


app.run(host='0.0.0.0')