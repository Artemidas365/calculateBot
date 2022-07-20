import telebot
import datetime
from config import Token
from funcs import calculator, in_days, in_seconds, in_hours, in_weeks
from telebot import types


bot = telebot.TeleBot(Token)
date = None
indays = None
insecs = None
inhours = None
inweeks = None
dmy = None


@bot.message_handler(commands=['start'])
def start(message):
    msg = "<b>hello</b>, I'm new bot"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton("Calculate age 📆")
    markup.add(itembtn1)
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def time_calculator(message):
    global date
    global indays
    global insecs
    global inhours
    global inweeks
    global dmy
    if message.text == "Calculate age 📆":
        markup = types.ReplyKeyboardRemove()
        msg = "Send me your birthday date\nIn format DD.MM.YYYY"
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif (message.text[2] and message.text[5] == '.') and len(message.text) == 10:
        date = message.text
        now = str(datetime.date.today())
        days, months, years = calculator(date, now)
        dmy = str(days) + ' days, ' + str(months) + ' months and ' + str(years) + ' years'
        # str(days), 'days', str(months), 'months', str(years), 'years'
        print(dmy)
        # print(days, 'days', months, 'months', years, 'years')
        indays = in_days(days, months, years)
        insecs = in_seconds(indays)
        inhours = in_hours(indays)
        inweeks = in_weeks(indays)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("In seconds ⌛")
        itembtn2 = types.KeyboardButton("In hours ⌚")
        itembtn3 = types.KeyboardButton("In days 📆")
        itembtn4 = types.KeyboardButton("In weeks 📅")
        itembtn5 = types.KeyboardButton("days, months and years")
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
        msg = "So, what scale would we use? 📏"
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif message.text == "In seconds ⌛":
        msg = str(insecs) + ' seconds'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Calculate age 📆")
        markup.add(itembtn1)
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif message.text == "In hours ⌚":
        msg = str(inhours) + ' hours'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Calculate age 📆")
        markup.add(itembtn1)
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif message.text == "In days 📆":
        msg = str(indays) + ' days'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Calculate age 📆")
        markup.add(itembtn1)
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif message.text == "In weeks 📅":
        msg = str(inweeks) + ' weeks'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Calculate age 📆")
        markup.add(itembtn1)
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    elif message.text == "days, months and years":
        msg = str(dmy)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Calculate age 📆")
        markup.add(itembtn1)
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')

    else:
        print('error')


bot.infinity_polling()
