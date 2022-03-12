# in the name of god

from pyrogram import Client
from pyrogram.types import *
import COVID19Py

#-------------------------# اطلاعات #-------------------------#
bot = Client(

    session_name= "mybot",
    api_id= 19007374,
    api_hash= "cf5da0ea280cf21ad6aa6f9850913b8d", # +380945159650
    bot_token= "5278385593:AAE5fZIZhZRAwNc1jmIIVRmVpRKsT4XPU_w"

)
#-------------------------# start #-------------------------#
def start(client , call):
    
    chat_id = call.from_user.id

    keyboard = ReplyKeyboardMarkup(keyboard=[

        
            ['music 🎵' , 'wallpaper 🖼' , 'covid 19 🦠'],
            ['about 🔎']


    ] , resize_keyboard=True)


        

    bot.send_message(chat_id , 'سلام `%s` به ربات ما خوش آمدید' %(call.from_user.first_name) , reply_markup=keyboard)

#-------------------------# music #-------------------------#
def music1(client , message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'لطفا صبر کنید')
    bot.send_document(chat_id , 'C:/Users/HAMAHANG/Downloads/file/sasy.mp3' , caption='اهنگ جدید ساسی')

#-------------------------# wallpaper #-------------------------#
def wallpaper(client , message):
    chat_id = message.chat.id
    bot.send_message(chat_id , 'لطفا صبر کنید')
    bot.send_document(chat_id, 'C:/Users/HAMAHANG/Downloads/file/foto.png' , caption='بیا اینم عکس')
#-------------------------# covid 19 #-------------------------#
def covid19(client , message):
    chat_id = message.chat.id
    text = bot.send_message(chat_id , 'چند لحظه صبر کنید')
    covid19 = COVID19Py.COVID19()
    location = covid19.getLocationByCountryCode("IR")
    
    for i in location:
        bot.edit_message_text(chat_id, text.message_id , f'''
        
    آمار کرونای ایران

    کشور : {i['country']}

    آخرین بروزرسانی : {i['last_updated']}

    مبتلایان : {i['latest']['confirmed']}

    فوت شدگان : {i['latest']['deaths']}
        
        ''')
#-------------------------# about #-------------------------#
def about(client , message):
    chat_id = message.from_user.id

    bot.send_message(chat_id, '''
    
    ربات فعلن در حال ساخت است 🚀

سازنده : @hassan_baba

این ربات فعلن هیچ موضوعی ندارد 😂

لطفا صبر کنید تا ربات کامل شود 😋

با تشکر %s
    
    ''' %(message.from_user.first_name))
#-------------------------# bot main #-------------------------#
@bot.on_message()
def main(client , message):

    text = message.text

    if text == '/start':
        start(client , message)
    elif text == 'music 🎵':
        music1(client, message)
    elif text == 'wallpaper 🖼':
        wallpaper(client, message)
    elif text == 'covid 19 🦠':
        covid19(client, message)
    elif text == 'about 🔎':
        about(client, message)
bot.run()