import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from re import search
from urllib.parse import urljoin, urlparse

BOT_TOKEN = "token"   # enter your telegram bot token



def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! I can \n [1] change Bundle-ID /cmd1 \n [2] change App-Name \n [3] change App-Version \n [4] change App-Icon & App-Name \n [5] change App Icon \n [6] inject Satella Jailed")


def request_handler(update: Update, context: CallbackContext):
    update.message.reply_text("You selected 'change Bundle-ID'\n send a iPA to continiue")




# Set up the Telegram bot
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the request handler to the dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('request', request_handler))
dispatcher.add_handler(CommandHandler('r', request_handler))

# Start the bot
updater.start_polling()
