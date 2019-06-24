import cv2
import numpy as np
from datetime import datetime, timedelta

def convert_time_to_string(dt):
    return str(dt.hour)+":"+str(dt.minute)
    
def get_black_background():
    return np.zeros((500, 500))
    
start_time = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    #convert_time_to_string(datetime.now()
    return image
    
def create_image_name(time):
    return str("r'"+"time_images" + time + ".jpg'")
    
while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    #path='D:/avatar/time_images'
    image_name=create_image_name(text)
    print(image_name)
    cv2.imwrite(image_name, image)
    start_time += timedelta(minutes=1)