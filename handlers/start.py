from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater

CALLBACK = 0  # Or define it in a central location

async def start(update: Updater, context: CallbackContext) -> int:
    """Start the conversation and display the main menu."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to AI Robot!🤖 We are thrilled to have you here and we have a variety of tools that can help you reach your objectives. If you have any queries or need help, please do not hesitate to contact us. We appreciate you choosing AI Robot!",
        reply_markup=start_menu_keyboard(),
    )
    return CALLBACK

def start_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📝 AI-Writer", callback_data='ai_writer'),
            InlineKeyboardButton("🎧 AI-Listener", callback_data='ai_listener'),
        ],
        [
            InlineKeyboardButton("📖 AI-Reader", callback_data='ai_reader'),
            InlineKeyboardButton("🖥️ Capture Web", callback_data='ai_capture'),
        ],
        [
            InlineKeyboardButton("🔗 URL Shortener", callback_data='url_shortener'),
            InlineKeyboardButton("📧 Mail", callback_data='mail'),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data='2'),
            InlineKeyboardButton("1", callback_data='1'),
            InlineKeyboardButton("➡️", callback_data='2'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def first(update: Updater, context: CallbackContext) -> int:
    """Display the first menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Welcome to AI Robot!🤖 We are thrilled to have you here and we have a variety of tools that can help you reach your objectives. If you have any queries or need help, please do not hesitate to contact us. We appreciate you choosing AI Robot!",
        reply_markup=first_menu_keyboard(),
    )
    return CALLBACK

def first_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📝 AI-Writer", callback_data='ai_writer'),
            InlineKeyboardButton("🎧 AI-Listener", callback_data='ai_listener'),
        ],
        [
            InlineKeyboardButton("📖 AI-Reader", callback_data='ai_reader'),
            InlineKeyboardButton("🖥️ Capture Web", callback_data='ai_capture'),
        ],
        [
            InlineKeyboardButton("🔗 URL Shortener", callback_data='url_shortener'),
            InlineKeyboardButton("📧 Mail", callback_data='mail'),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data='2'),
            InlineKeyboardButton("1", callback_data='1'),
            InlineKeyboardButton("➡️", callback_data='2'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def second(update: Updater, context: CallbackContext) -> int:
    """Display the second menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Welcome to AI Robot!🤖 We are thrilled to have you here and we have a variety of tools that can help you reach your objectives. If you have any queries or need help, please do not hesitate to contact us. We appreciate you choosing AI Robot!",
        reply_markup=second_menu_keyboard(),
    )
    return CALLBACK

def second_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🔒 Encrypt", callback_data='encrypt_menu'),
            InlineKeyboardButton("🔓 Decrypt", callback_data='decrypt_menu'),
        ],
        [
            InlineKeyboardButton("📝 Speech to Text", callback_data='speech_to_text'),
            InlineKeyboardButton("📝 Web Scrape", callback_data='web_scrape'),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data='1'),
            InlineKeyboardButton("2", callback_data='2'),
            InlineKeyboardButton("➡️", callback_data='1'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def cancel(update: Updater, context: CallbackContext) -> int:
    """Cancel the current operation and return to the main menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Welcome to AI Robot! 🤖 We are delighted to have you here and would like to let you know that we have a wide range of tools that can help you achieve your goals. Please do not hesitate to reach out to us if you have any questions or need assistance. Thank you for choosing AI Robot!",
        reply_markup=start_menu_keyboard(),
    )
    return CALLBACK