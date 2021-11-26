from typing import Text
from pyrogram import Client,filters
import os
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")
last_id=str()
message_id=str()
@app.on_message(filters.me)
def ocr(client, message):
    global last_id
    global message_id
    message_id=message.message_id
    last_id = message.chat.id
    text=message.text
    text2=text.split()[0]
    if text2=="!ocr":
        text=message.reply_to_message.photo.file_id
        client.download_media(text,"test.jpg")
        client.send_photo("ocr_prov_bot","downloads/test.jpg")
        os.remove("downloads/test.jpg")
       
@app.on_message(filters.chat(2143804610))
def forward(client,message):
    text=message.text
    client.send_message(chat_id=last_id,text=text,reply_to_message_id=message_id)
app.run()