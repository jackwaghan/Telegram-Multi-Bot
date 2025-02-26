from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
from telegram.constants import ParseMode
from config import key
from cryptography.fernet import Fernet
from keyboards import encrypt_decrypt as encrypt_decrypt_keyboards

ENCRYPT = 10 # Define the state
DECRYPT = 11 # Define the state

fernet = Fernet(key.encode())

async def encrypt_menu(update: Updater, context: CallbackContext) -> int:
    """Display the encrypt menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🔒Encrypt\nSend the text that you want to encrypt (Decryption only done by this bot)",
        reply_markup=encrypt_decrypt_keyboards.encrypt_keyboard(),
    )
    return ENCRYPT

async def encrypt(update: Updater, context: CallbackContext) -> int:
    """Encrypt the given text."""
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔒_encrypting..._",
        parse_mode=ParseMode.MARKDOWN,
    )

    # Get the message text
    message_text = update.message.text

    # Api
    encrypted = fernet.encrypt(bytes(message_text, "utf-8"))
    encrypt = str(encrypted, "utf8")

    # Send the response to the chat
    await context.bot.edit_message_text(
        chat_id=update.effective_chat.id,
        message_id=message.message_id,
        text=encrypt,
        reply_markup=encrypt_decrypt_keyboards.encrypt_after_keyboard(),
    )
    return 0 # Replace CALLBACK with the actual value

async def decrypt_menu(update: Updater, context: CallbackContext) -> int:
    """Display the decrypt menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🔓Decrypt\nSend the text that you want to decrypt",
        reply_markup=encrypt_decrypt_keyboards.decrypt_keyboard(),
    )
    return DECRYPT

async def decrypt(update: Updater, context: CallbackContext) -> int:
    """Decrypt the given text."""
    try:
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🔓_decrypting..._",
            parse_mode=ParseMode.MARKDOWN,
        )
        # Get the message text
        message_text = update.message.text

        # Api
        decrypted = fernet.decrypt(bytes(message_text, "utf-8"))
        decrypt = str(decrypted, "utf8")

        # Send the response to the chat
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text=decrypt,
            reply_markup=encrypt_decrypt_keyboards.decrypt_after_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value

    except Exception as e:
        print(f"Decryption error: {e}")  # Log the error
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="🔓_Invalid key_",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=encrypt_decrypt_keyboards.decrypt_after_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value