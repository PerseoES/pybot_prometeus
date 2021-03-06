 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import os

from flask import Flask, request
import respuestas as R
import telebot
from telebot import types
import time


TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

markup = types.InlineKeyboardMarkup()
item1=types.InlineKeyboardButton("Mi Linkedin", url="https://linkedin.com/in/emiliano-pintos")
item2=types.InlineKeyboardButton("Mi Instagram", url="https://instagram.com/sebasti4n.ps")
markup.add(item1, item2)


@bot.message_handler(commands=['contacto'])
def contacto(message):
    bot.send_message(message.chat.id, "Contactame por aquí:", reply_markup=markup)

@bot.message_handler(commands=['comenzar'])
def start(message):
    bot.reply_to(message, 'Comencemos, ' + message.from_user.first_name)

def buscartxt(msg):
    for letra in msg:
        if '@' in letra:
            return msg

@bot.message_handler(commands=['saludar'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola, soy Lemillion Bot.
Estoy aquí para realizar lo que me digas, sólo envíame un mensaje y te responderé...
PD: Espera a que sea programado para que pueda realizar otra acción!\
""")    


@bot.message_handler(func=lambda msg: msg.text is not None and 'p' in msg.text)
def promedio(message):
    resultado = prom(message)
    bot.reply_to(message, resultado)
    
    
@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def crearlinkig(message):
    bot.reply_to(message, 'Ingresa un usuario de IG y te devolveré su link a continuación (ej. @user).')
    msj=message.text.split()
    var = buscartxt(msj)
    bot.reply_to(message, 'https://instagram.com/{}'.format(map(var)))


@bot.message_handler(commands=['saludar'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola, soy Lemillion Bot.
Estoy aquí para realizar lo que me digas, sólo envíame un mensaje y te responderé...
PD: Espera a que sea programado para que pueda realizar otra cosa!\
""")


    
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    texto = str(message.text).lower()
    resp = R.resp_simples(texto)
    bot.reply_to(message, resp)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://py-bot-prometeus.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
