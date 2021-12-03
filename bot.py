from googletrans import Translator
from typing import Text
from gtts import gTTS
from pyrogram import Client,filters
import os
import requests
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")
last_id=str()
message_id=str()
@app.on_message(filters.regex("^!ocr$") & (filters.user(760148720) | filters.me))
def ocr(client,message):
    global last_id
    global message_id
    message_id=message.message_id
    last_id = message.chat.id
    text=message.reply_to_message.photo.file_id
    client.download_media(text,"test.jpg")
    client.send_photo("ocr_prov_bot","downloads/test.jpg")
    os.remove("downloads/test.jpg")

@app.on_message(filters.regex("^!trans ") & (filters.user(760148720) | filters.me))
def ocr(client,message):
    text=message.text 
    text2=text.split()[0]
    text=text.replace(text2,"")
    mas_id=message.message_id
    src=text.split()[0]
    text=text.replace(src,"")
    dest=text.split()[0]
    text=text.replace(dest,"")
    translator = Translator()
    result = translator.translate(text, src=src,dest=dest)
    client.send_message(chat_id=message.chat.id,text=result.text,reply_to_message_id=mas_id)

@app.on_message(filters.regex("^!tts$") & (filters.user(760148720) | filters.me))
def tts(client,message):
    chat_id=message.chat.id
    message_id=message.message_id
    text = message.reply_to_message.text
    language="en"
    myobj=gTTS(text=text,lang=language,slow=False)
    myobj.save("test.ogg")
    client.send_audio(chat_id,"test.ogg",reply_to_message_id=message_id)
    os.remove('test.ogg')

    
@app.on_message(filters.chat(2143804610))
def forward(client,message):
    text=message.text
    client.send_message(chat_id=last_id,text=text,reply_to_message_id=message_id)
app.run()
