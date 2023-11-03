import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
import csv
from pars import *

bot = telebot.TeleBot('6521711847:AAFP5bytPFGVZpj9LqPpuJwWPv_NlZv2o4U')

# keyboard = types.ReplyKeyboardMarkup()

# button = types.KeyboardButton('Description')
# button2 = types.KeyboardButton('Quit')

# keyboard.add(button)
# keyboard.add(button2)


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Введите любое сообщение чтобы увидеть результаты парсинга')
    bot.register_next_step_handler(message, func)
    bot.register_next_step_handler(message, description)
    bot.register_next_step_handler(message, choose_news)


def func(message):
    with open('news_list.csv','r') as f_main:
        csvreader = csv.reader(f_main)
        count = 1
        for i in csvreader:
            i_i = str(i[0]).split('|')
            if count == 21:
                break
            bot.send_message(message.chat.id,f'/{count}. {i_i[0]}')
            count += 1


def description(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Description")
    btn2 = types.KeyboardButton("/Quit")
    markup.add(btn1, btn2)
    send_href = ''
    send_img = ''
    with open('news_list.csv','r') as f_main:
            csvreader = csv.reader(f_main)
            count = 1
            for i in csvreader:
                if f'/{count}' == message.text:
                    i_i = str(i[0]).split('|')
                    send_href = f'{i_i[2]}'
                    send_img = f'{i_i[1]}'
                count += 1

    bot.send_message(message.chat.id,'some title news you can see Description of this news and Photo',reply_markup=markup)



@bot.message_handler(commands=[f'{i}' for i in range(1,21)])
def choose_news(message):
    with open('news_list.csv','r') as f_main:
        csvreader = csv.reader(f_main)
        count = 1
        for i in csvreader:
            if f'/{count}' == message.text:
                print(i)
                i_i = str(i)[1:-1].split('|')
                bot.send_message(message.chat.id,f'{i_i[-1]}')
                bot.send_message(message.chat.id,{i_i[1]})
            count += 1
   

bot.polling()
main()