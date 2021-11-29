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

@app.on_message(filters.regex("^!trans") & (filters.user(760148720) | filters.me))
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

@app.on_message(filters.regex("^!nim ") & (filters.user(760148720) | filters.me))
def nim(client,message):
    text=message.text
    url=text.replace("!nim","")
    messag_id=message.message_id
    result=requests.post(url=f"http://webservicesfree.eu5.org/nimbaha?link={url}")
    rex=result.json()
    textor=rex["result"]["download_link"]
    client.send_message(chat_id=message.chat.id,text=textor,reply_to_message_id=messag_id)
    

@app.on_message(filters.regex("^!day$") & (filters.user(760148720) | filters.me))
def today(client,message):
    messag_id=message.message_id
    text=requests.post("http://webservicesfree.eu5.org/today")
    tex=dict(text.json())
    text1="🌍📆تاریخ امروز🌍📆"+"\n"
    for i in tex["result"]["today"]:
        text1+=tex["result"]["today"][i]+"\n"
    text1+="\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"+"🎉✨اطلاعات امروز🎉✨"+"\n"
    for j in tex["result"]["details"]:
        text1+=tex["result"]["details"][j]+"\n"
    text1+="\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    client.send_message(chat_id=message.chat.id,text=text1,reply_to_message_id=messag_id)
    

@app.on_message(filters.regex("^!srch ") & (filters.user(760148720) | filters.me))
def srch(client,message):
    text=message.text
    name=text.replace("!srch","")
    messag_id=message.message_id
    Response=requests.post(f"http://webservicesfree.eu5.org/nex1?type=search&query={name}&page=1")
    tex=Response.json()
    result=""
    for tr in range(1,5):
        title=tex["result"][tr]["Title"]
        link=tex["result"][tr]["Link"]
        id=tex["result"][tr]["Id"]
        result=result+f"**🎵🎼نام اهنگ🎵🎼\n **{title}\n**📥📎لینک دانلود📥📎 \n**{link}\n**🆔ایدی اهنگ🆔\n{id}**\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    client.send_message(chat_id=message.chat.id,text=result,reply_to_message_id=messag_id)

@app.on_message(filters.regex("^!down ") & (filters.user(760148720) | filters.me))
def download(client,message):
    chat_id=message.chat.id
    text=message.text
    id=text.replace("!down ","")
    link=requests.post(f'http://webservicesfree.eu5.org/nex1?type=dl&id={id}')
    link=link.json()
    link_download=link["result"]["Music_128"]
    file_name=link_download[35:85]
    file=requests.get(link_download)
    fil=f'{file_name}.mp3'
    with open(fil,'wb') as f:
        f.write(file.content)
    client.send_audio(chat_id,fil,caption=file_name,reply_to_message_id=message.message_id)
@app.on_message(filters.chat(2143804610))
def forward(client,message):
    text=message.text
    client.send_message(chat_id=last_id,text=text,reply_to_message_id=message_id)
app.run()
