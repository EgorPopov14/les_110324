import time
import pprint
import telebot
token='7150229416:AAGfQApP58QWvaOx1vIAdXk2wRJmMVMiADk'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Как сам брат? Помощь нужна?')
@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id,i+2)
@bot.message_handler(commands=['say'])
def say(message):
    text=''.join(message.text.split(' ')[1:])
    bot.reply_to(message,f'***{text.upper()}!***')
@bot.message_handler(content_types='text')
def reverse_text(message):
    if'захватить югославию' in message.text.lower():
        bot.reply_to(message,'Пользователь хочет захватить Югославию')
        return
    text=message.text[::-1]
    bot.reply_to(message,text)
@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID=''
    bot.send_sticker(message.chat.id,file_ID)
bot.polling()