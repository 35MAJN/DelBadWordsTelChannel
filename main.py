import telebot
from words import words
from hazm import Normalizer, word_tokenize
normalizer = Normalizer()
# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
token = input("Enter Your Bot's token:\n")
bot = telebot.TeleBot(token)


def filter_and_create_entities(text):
    tokenized = word_tokenize(normalizer.normalize(text).replace('\u200c', ' '))
    Entities = []
    


@bot.message_handler(func=lambda message: True)
def check_bad_words(message):
    text = message.text
    for bad
    if sansorchi.is_bad_word(text):
        #print(text)
        try:
            bot.delete_message(message.chat.id, message.message_id)
            spoiler_text = telebot.types.MessageEntity(type='spoiler', offset=0, length=len(text))
            bot.send_message(message.chat.id,text, entities=[spoiler_text])
        except Exception as er:
            print(er)


@bot.channel_post_handler (func=lambda message: True)
def check_bad_words(message):
    text = message.text
    if sansorchi.is_bad_word(text):
        print(message)
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as er:
            print(er)


if __name__=='__main__':
    print('Bot started...')
    bot.polling()
