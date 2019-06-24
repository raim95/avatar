#!/usr/bin/python3

from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
#from .utils import *
from telethon import TelegramClient, sync
#from .config import *

api_ip=777156
api_hash=112a5cf7176b11914bfc0e47909d408a

def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"

def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time

client = TelegramClient(change_my_avatar, api_id, api_hash)
client.start()

while True:
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(datetime.now())
        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))
