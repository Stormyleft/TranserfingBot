
import telebot

import constants
import log_maker

log = log_maker.log
stats = log_maker.stats

bot = telebot.TeleBot(constants.token_Nick420)


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def default_command(message):
    log(message)
    bot.send_message(message.chat.id, "получен")
    if message.text == 'shit':
        stats(message)

bot.polling()
