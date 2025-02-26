from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import donate, contact

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📩 Contact", url=f'{contact}'),
            InlineKeyboardButton("🆔 Find Telegram ID", url=f'{contact}')
        ],
        [
            InlineKeyboardButton("💸 Pay", url=f'{donate}'),
            InlineKeyboardButton("🏠 Home", callback_data='cancel')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)