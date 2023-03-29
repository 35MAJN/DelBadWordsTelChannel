import telebot
from words import words
from hazm import Normalizer, word_tokenize
import itertools
normalizer = Normalizer()
# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
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
    tokenized = word_tokenize(normalizer.normalize(text).replace('\u200c', ' '))
    Entities = []
    has_bad_word = False
    for word in tokenized:
        _word = ''.join(ch for ch, _ in itertools.groupby(word))
        for badword in words:
            if badword in _word and word != 'کسی':
                has_bad_word = True
                Entities.append(telebot.types.MessageEntity(type='spoiler', offset=text.find(word), length=len(word)))
    return Entities, has_bad_word
    


@bot.message_handler(func=lambda message: True)
def check_bad_words(message):
    text = message.text
    Entities, has_bad_word= detect_bad_words(text)
    if has_bad_word:
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id,text, entities=Entities)
        except Exception as er:
            print(er)


@bot.channel_post_handler (func=lambda message: True)
def check_bad_words(message):
    text = message.text
    Entities, has_bad_word= detect_bad_words(text)
    if has_bad_word:
        try:
            bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, entities=Entities)
        except Exception as er:
            print(er)


if __name__=='__main__':
    print('Bot started...')
    bot.polling()
