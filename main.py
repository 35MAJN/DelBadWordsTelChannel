import telebot
from words import *
from hazm import Normalizer, word_tokenize
import re
import itertools
import argparse

# create a new ArgumentParser
parser = argparse.ArgumentParser()

# add the argument
parser.add_argument('-i', '--input', help='TOKEN')

# parse the arguments
args = parser.parse_args()


normalizer = Normalizer()
# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
if args.input:
    token = args.input
else:
    token = input("Enter Your Bot's token:\n")
bot = telebot.TeleBot(token)


def detect_bad_words(text):
    """
    Detects bad words in the given text and returns the list of spoiler message entities for those words along with a boolean value indicating if any bad words were found.

    Parameters:
        text (str): The text in which to search for bad words.
        
    Returns:
        Tuple[List[telebot.types.MessageEntity], bool]: A tuple containing the list of spoiler message entities for bad words in the text and a boolean value indicating if any bad words were found.
        
    Example:
        text = "I can't believe he said that! Fuc*"
        Entities, has_bad_word = detect_bad_words(text)
        has_bad_word
        True
        Entities
        [telebot.types.MessageEntity(type='spoiler', offset=30, length=4)]

    """
    tokenized = word_tokenize(re.sub(r'[^\w]', ' ', normalizer.normalize(text).replace('\u200c', ' ')))
    clean_text = re.sub(r'[^\w]', ' ', text.replace('\u200c', ' '))
    Entities = []
    has_bad_word = False
    has_holly_word = False
    for word in tokenized:
        _word = ''.join(ch for ch, _ in itertools.groupby(word))
        for badword in words:
            if badword in _word or _word in exactbadwords:
                has_bad_word = True
                Entities.append(telebot.types.MessageEntity(type='spoiler', offset=text.find(word), length=len(word)))
    
    for holly_word in hollywords:
        if holly_word in clean_text:
            has_holly_word = True
    return Entities, has_bad_word, has_holly_word
    


@bot.message_handler(func=lambda message: True)
def check_bad_words(message):
    text = message.text
    Entities, has_bad_word, has_holly_word= detect_bad_words(text)
    if has_bad_word:
        if has_holly_word:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception as er:
                print(er)
        else:
            try:
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id,text, entities=Entities)
            except Exception as er:
                print(er)


@bot.channel_post_handler (func=lambda message: True)
def check_bad_words(message):
    text = message.text
    Entities, has_bad_word, has_holly_word= detect_bad_words(text)
    if has_bad_word:
        if has_holly_word:
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except Exception as er:
                print(er)
        else:
            try:
                bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, entities=Entities)
            except Exception as er:
                print(er)


if __name__=='__main__':
    print('Bot started...')
    while True:
        try:
            bot.polling()
        except Exception as er:
                print(er)
            
