# Telegram Bot for Filtering Bad Words in Persian
This Python code provides a Telegram bot that can be used to filter out messages containing bad words in Persian. The bot uses the sansorchi library to detect and remove messages that contain bad words.

## Prerequisites
 - Python 3.6 or higher
 - Telegram Bot API token
 - telebot library
 - hazm library
 - argparse
 
## Installation
 - Clone the repository or download the code. 
 - Install the required libraries using ```pip install -r requirements.txt```.
 - Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token in the bot instantiation.
 - Run the script using python main.py.
 - Enter your Telegram token when prompted.


## Usage
 To run the script, navigate to the directory where it is located and execute the following command:
```python script_name.py -i YOUR_TELEGRAM_BOT_TOKEN```
Or you can run the script without -i argument and the script will ask for the token.

The bot will start running and will monitor all incoming messages in the chat or channel that it has been added to. If it detects any bad words, it will delete the message and replace the bad word with a spoiler message entity. If the message contains both bad words and holy words it will not delete the message but instead delete the message silently so the user can not recognize it was deleted.

## Notes
 - This code is designed to filter out bad words in Persian only. If you want to filter out bad words in other languages, you may need to use a different library or modify the code to suit your needs.
