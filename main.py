import telebot
from sansorchi import Sansorchi

sansorchi = Sansorchi()

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
token = input("Enter Your Bot's token:\n")
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda message: True)
def check_bad_words(message):
    text = message.text
    if sansorchi.is_bad_word(text):
        print(text)
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as er:
            print(er)


@bot.channel_post_handler (func=lambda message: True)
def check_bad_words(message):
    text = message.text
    if sansorchi.is_bad_word(text):
        print(text)
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as er:
            print(er)


if __name__=='__main__':
    print('Bot started...')
    bot.polling()
