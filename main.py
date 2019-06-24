from telethon import TelegramClient, sync
from .config import *

client = TelegramClient(change_my_avatar, api_id, api_hash)
client.start()