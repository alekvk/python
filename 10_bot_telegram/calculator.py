import telebot
import random
from telebot import types
import spy

bot = telebot.TeleBot("5892902177:AAHmlLBwT8SPLAKNEiZDO70CCd_MLdJCW7k")

typeNums = 0


@bot.message_handler(commands=["start"])
def calc(message):
    spy.log(message)
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Рациональные')
    key2 = types.KeyboardButton('Комплексные')
    mrk.add(key1, key2)
    bot.send_message(message.chat.id, f'Калькулятор \nСделайте выбор, с какими числами работать', reply_markup=mrk)

@bot.message_handler(content_types=['text'])
def buttons(message):
    spy.log(message)
    global typeNums
    a = types.ReplyKeyboardRemove()
    if message.text == 'Рациональные':
        bot.send_message(message.chat.id, f'Выбран режим рациональных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 0
    elif message.text == 'Комплексные':
        bot.send_message(message.chat.id, f'Выбран режим комплексных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 1

def controller(message):
    spy.log(message)
    line = message.text.split()
    znak = line[1]
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])
    if znak == '+':
        res = summ_nums(a, b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == '//' or znak == '%'):
        bot.send_message(message.chat.id, f'Неверный ввод, повторите')
        bot.register_next_step_handler(message, controller)
        return
    elif znak == '//':
        res = div_int(a, b)
    elif znak == '%':
        res = div_rem(a, b)
    bot.send_message(message.chat.id, str(res))

def summ_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def mult_nums(a, b):
    return a * b

def div_nums(a, b):
    return a / b

def div_int(a, b):
    return a // b

def div_rem(a, b):
    return a % b

bot.infinity_polling()









