import asyncio
import logging
import os

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

import config
from handlers import start, ai_writer, ai_listener, ai_capture, mail, shortener, encrypt_decrypt 
from keyboards import main_menu
from google.cloud import speech
from bs4 import BeautifulSoup
import requests

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define states (if you haven't already)
(
    MAIL,
    SHORTENER,
    MESSAGE,
    TO,
    WRITER,
    READER,
    LISTENER,
    CALLBACK,
    CAPTURE,
    ENCRYPT,
    DECRYPT,
    SPEECH_TO_TEXT,
    WEB_SCRAPE,
) = range(13)

def main():
    application = ApplicationBuilder().token(config.bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start.start)],
        states={
            CALLBACK: [
                CallbackQueryHandler(encrypt_decrypt.encrypt_menu, pattern='encrypt_menu'),
                CallbackQueryHandler(encrypt_decrypt.decrypt_menu, pattern='decrypt_menu'),
                CallbackQueryHandler(ai_capture.ai_capture, pattern='ai_capture'),
                CallbackQueryHandler(ai_listener.ai_listener, pattern='ai_listener'),
                # CallbackQueryHandler(ai_reader.ai_reader, pattern='ai_reader'),
                CallbackQueryHandler(ai_writer.ai_writer, pattern='ai_writer'),
                CallbackQueryHandler(mail.mail, pattern='mail'),
                CallbackQueryHandler(shortener.shortener, pattern='url_shortener'),
                CallbackQueryHandler(start.first, pattern='1'),
                CallbackQueryHandler(start.second, pattern='2'),
                CallbackQueryHandler(ai_writer.speech_to_text, pattern='speech_to_text'),
                CallbackQueryHandler(ai_writer.web_scrape, pattern='web_scrape'),
            ],
            ENCRYPT: [MessageHandler(filters.TEXT, encrypt_decrypt.encrypt)],
            DECRYPT: [MessageHandler(filters.TEXT, encrypt_decrypt.decrypt)],
            CAPTURE: [MessageHandler(filters.TEXT, ai_capture.capture)],
            LISTENER: [MessageHandler(filters.TEXT, ai_listener.listener)],
            WRITER: [MessageHandler(filters.TEXT, ai_writer.writer)],
            TO: [MessageHandler(filters.TEXT, mail.to)],
            MESSAGE: [MessageHandler(filters.TEXT, mail.message)],
            SHORTENER: [MessageHandler(filters.TEXT, shortener.shortener_url)],
            SPEECH_TO_TEXT: [MessageHandler(filters.AUDIO, ai_writer.speech_to_text_file)],
            WEB_SCRAPE: [MessageHandler(filters.TEXT, ai_writer.web_scarpe_file)],
        },
        fallbacks=[CallbackQueryHandler(start.cancel, pattern='cancel')],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('start', start.start))

    application.run_polling()

if __name__ == '__main__':
    main()