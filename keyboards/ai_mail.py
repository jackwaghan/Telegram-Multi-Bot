from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate

def ai_mail_per_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=F'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data='mail'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def mail_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)