# -*- coding: utf-8 -*-
# Bot

import random

import telebot

import constants
import texts
import log_maker

log = log_maker.log
audio_log = log_maker.new_book_log
stats = log_maker.stats

bot = telebot.TeleBot(constants.token_Transerfing)


# Отправка клавиатуры меню
def books_markup():
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for i in texts.books:
        m.row(i)
    return m


# Отправка клавиатуры подменю
def parts_markup(ind):
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for i in texts.books_parts[ind].keys():
        m.row(i)
    m.row(texts.back_button)
    return m


@bot.message_handler(commands=['start', 'help'])
def hendler_start_message(message):
    log(message)
    if message.text == '/start':
        bot.send_message(message.from_user.id, texts.start_message,  reply_markup=books_markup())
    elif message.text == '/help':
        pass


@bot.message_handler(content_types=['text', 'audio'])
def hendler_text(message):
    log(message)
    if False:
        pass
    elif texts.books.count(message.text) != 0:
        ind = texts.books.index(message.text)
        r = random.randrange(0, len(texts.books_message))
        bot.send_message(message.from_user.id, texts.books_message[r],  reply_markup=parts_markup(ind))
    elif texts.all_parts_keys.count(message.text) != 0:
        bot.send_audio(message.from_user.id, texts.all_parts[message.text],)
        stats(message)
    elif message.text == texts.back_button:
        bot.send_message(message.from_user.id, texts.back_message,  reply_markup=books_markup())
    if message.audio is not None:
        audio_log(message.audio.title, message.audio.file_id)


bot.polling(none_stop='True', interval=0)

"""
Все что после, не выполняется
"""
