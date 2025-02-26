from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate

def ai_writer_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)

def ai_writer_per_keyboard():
    keyboard = [[
        InlineKeyboardButton("💝 Donate", url=f'{donate}')
    ], [
        InlineKeyboardButton("🔁 Again", callback_data='ai_writer'),
        InlineKeyboardButton("🏠 Home", callback_data='cancel')
    ]]
    return InlineKeyboardMarkup(keyboard)

def speech_to_text_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)

def speech_to_text_per_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=F'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data="speech_to_text"),
            InlineKeyboardButton("🏠 Home", callback_data="cancel"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def web_scrape_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)

def web_scrape_per_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=F'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data="web_scrape"),
            InlineKeyboardButton("🏠 Home", callback_data="2"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)