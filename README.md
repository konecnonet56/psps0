import telebot

bot = telebot.TeleBot('7814928681:AAFsgXNtWaBhtFGt7HGjCiowFm2Vjhe-fB8')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот дает локацию по утелизации мусора в Магадане. По комманде /loc он отправляет локацию ,где можно отдать ваш мусор на утелизацию")
@bot.message_handler(commands=['loc'])
def send_loc(message):
    bot.send_message(message.chat.id,'геопозиция одного из мест:')
    blaba = 59.571336
    bebe = 150.810194
    bot.send_location(message.chat.id,latitude= blaba ,longitude=bebe )
bot.polling()
