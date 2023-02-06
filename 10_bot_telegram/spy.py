import telebot
from telebot import types
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def log(message):
    file = open('db.txt', 'a')
    #file.write(f'{datetime.datetime.now().time()}, {message.chat.username}, {message.chat.id} {message.text}\n')

    file.write(f'{datetime.datetime.now()} {message.chat.username}  {message.chat.first_name}  '
               f'{message.chat.last_name}  {message.chat.id}  {message.text}\n')
    file.close()