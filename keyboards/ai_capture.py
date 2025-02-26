from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate

def ai_capture_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)

def ai_capture_per_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=f'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data='ai_capture'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)