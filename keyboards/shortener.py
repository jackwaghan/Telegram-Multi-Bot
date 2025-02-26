from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate

def shortener_per_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=F'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data='url_shortener'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def shortener_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)