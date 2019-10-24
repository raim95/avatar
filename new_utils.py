#!/usr/bin/python3

import cv2
import numpy as np
from datetime import datetime, timedelta

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"

def get_black_background():
    return np.zeros((500, 500))
    
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.05), int(image.shape[1]*0.58)), font, 5, (255, 0, 255), 2, cv2.LINE_AA)
    #convert_time_to_string(datetime.now()
    return image
    
def create_image_name(time):
    return str(time + ".jpg")
    
while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite(create_image_name(text), image)
    start_time += timedelta(minutes=1)

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
