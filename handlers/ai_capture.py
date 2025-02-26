from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
import requests
from telegram.constants import ParseMode
from config import capture_id
from utils import text_menu_message
from keyboards import main_menu
from keyboards import ai_capture as ai_capture_keyboards

CAPTURE = 8 # Define the state

async def ai_capture(update: Updater, context: CallbackContext) -> int:
    """Display the AI Capture menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Hello! I am a bot to capture web page.\n\nSend me a link to capture the web page.",
        reply_markup=ai_capture_keyboards.ai_capture_keyboard(),
    )
    return CAPTURE

async def capture(update: Updater, context: CallbackContext) -> int:
    """Capture the web page from the given URL."""
    try:
        if update.effective_chat.id in capture_id:
            global message
            message = await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="_Capturing..._",
                parse_mode=ParseMode.MARKDOWN,
            )
            # Get the message text
            message_text = update.message.text
            # send the message uploading...
            delete = await context.bot.edit_message_text(
                chat_id=update.effective_chat.id,
                message_id=message.message_id,
                text="_uploading..._",
                parse_mode=ParseMode.MARKDOWN,
            )
            url = "https://cloudlayer-io.p.rapidapi.com/v1/url/image"
            querystring = {"url": f"{update.message.text}"}
            headers = {
                "X-RapidAPI-Key": "393ec6a13bmsh7100c991461deefp1a176cjsn5a2e4e162f84",
                "X-RapidAPI-Host": "cloudlayer-io.p.rapidapi.com",
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring
            )

            await context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=response.content
            )
            # delete the message uploading...
            await context.bot.delete_message(
                chat_id=update.effective_chat.id, message_id=delete.message_id
            )
            # send the message done
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="What do you want to do next?",
                reply_markup=ai_capture_keyboards.ai_capture_per_keyboard(),
            )

            # Print the incoming Paid-user
            chat_user_id = update.effective_chat.id
            user_message = message_text
            user_user_name = update.effective_chat.username
            print(
                "Paid-User Client - {}, Chat ID - {}, Messaage - {}".format(
                    user_user_name, chat_user_id, user_message
                )
            )
            return 0 # Replace CALLBACK with the actual value

        # Send a message to the not paid chat
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_writing..._",
            parse_mode=ParseMode.MARKDOWN,
        )

        # Get the message text
        message_text = update.message.text
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text=text_menu_message(),
            reply_markup=main_menu.main_menu_keyboard(),
        )

        # Print the incoming user
        chat_user_id = update.effective_chat.id
        user_message = message_text
        user_user_name = update.effective_chat.username
        print(
            "User Client - {}, Chat ID - {}, Messaage - {}".format(
                user_user_name, chat_user_id, user_message
            )
        )

        return 0 # Replace CALLBACK with the actual value

    except Exception as e:
        print(f"Capture error: {e}")  # Log the error
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="Please send a valid link.",
            reply_markup=ai_capture_keyboards.ai_capture_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value