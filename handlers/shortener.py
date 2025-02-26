from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
import requests
from telegram.constants import ParseMode
from keyboards import shortener as shortener_keyboards

SHORTENER = 2 # Define the state

async def shortener(update: Updater, context: CallbackContext) -> int:
    """Display the URL Shortener menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🔗 Send me the URL you want to shorten.",
        reply_markup=shortener_keyboards.shortener_keyboard(),
    )
    return SHORTENER

async def shortener_url(update: Updater, context: CallbackContext) -> int:
    """Shorten the given URL."""
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="_Shortening..._",
        parse_mode=ParseMode.MARKDOWN,
    )

    url = "https://api.short.io/links"

    payload = {"domain": "link.jackwaghan.ml", "originalURL": f"{update.message.text}"}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "sk_8YbD8KOrPUV7jmfd",
    }

    response = requests.post(url, json=payload, headers=headers)

    url = response.json()["shortURL"]

    await context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=message.message_id,
        text="🔗 Here is your shortened URL:\n{}".format(url),
        reply_markup=shortener_keyboards.shortener_per_keyboard(),
    )
    return 0 # Replace CALLBACK with the actual value