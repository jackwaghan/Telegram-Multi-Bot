from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
import openai
import requests
from config import listener_id
from utils import text_menu_message
from keyboards import main_menu
from keyboards import ai_listener as ai_listener_keyboards

LISTENER = 6 # Define the state

async def ai_listener(update: Updater, context: CallbackContext) -> int:
    """Display the AI Listener menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Hello! I am a bot that integrates with the OpenAI GPT-3 and Built in Text to Speech API. You can ask me any question and I will try to provide a response.",
        reply_markup=ai_listener_keyboards.ai_listener_keyboard(),
    )
    return LISTENER

async def listener(update: Updater, context: CallbackContext) -> int:
    """Listen to the user's question and provide a response using OpenAI and Text to Speech API."""
    if update.effective_chat.id in listener_id:
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_listening..._",
            parse_mode=ParseMode.MARKDOWN,
        )
        # Get the message text
        message_text = update.message.text
        response = openai.Completion.create(
            engine="text-curie-001",
            prompt="{}".format(message_text),
            max_tokens=400,
            temperature=0.7,
        )
        mes = response["choices"][0]["text"]
        # send the message uploading...
        delete = await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="_uploading..._",
            parse_mode=ParseMode.MARKDOWN,
        )
        url = "https://text-to-speech27.p.rapidapi.com/speech"
        querystring = {f"text": {mes}, "lang": "en-us"}

        headers = {
            "X-RapidAPI-Key": "393ec6a13bmsh7100c991461deefp1a176cjsn5a2e4e162f84",
            "X-RapidAPI-Host": "text-to-speech27.p.rapidapi.com",
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring
        )

        await context.bot.send_audio(
            chat_id=update.effective_chat.id, audio=response.content, title="Speech"
        )
        # delete the message uploading...
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=delete.message_id
        )
        # send the message done
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="What do you want to do next?",
            reply_markup=ai_listener_keyboards.ai_listener_per_keyboard(),
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