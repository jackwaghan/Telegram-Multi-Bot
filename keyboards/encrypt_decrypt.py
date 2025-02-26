from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate

def encrypt_after_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=f'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data='encrypt_menu'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def encrypt_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)

def decrypt_after_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("💝 Donate", url=f'{donate}'),
        ],
        [
            InlineKeyboardButton("🔁 Again", callback_data='decrypt_menu'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

def decrypt_keyboard():
    keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data='cancel')]]
    return InlineKeyboardMarkup(keyboard)