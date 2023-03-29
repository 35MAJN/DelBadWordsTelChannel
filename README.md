# Telegram Bot for Filtering Bad Words in Persian
This Python code provides a Telegram bot that can be used to filter out messages containing bad words in Persian. The bot uses the sansorchi library to detect and remove messages that contain bad words.

## Prerequisites
 - Python 3.6 or higher
 - Telegram Bot API token
 - telebot library
 - sansorchi library
## Installation
 - Clone the repository or download the code.
 - Install the required libraries using pip install -r requirements.txt.
 - Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token in the bot instantiation.
 - Run the script using python main.py.
 - Enter your Telegram token when prompted.


## Usage
 - Once the bot is running, it will listen for new messages in any chat it is added to. If a message contains a bad word detected by sansorchi, the bot will automatically remove the message. The bot will run until it is stopped manually.

## Notes
 - This code is designed to filter out bad words in Persian only. If you want to filter out bad words in other languages, you may need to use a different library or modify the code to suit your needs.
