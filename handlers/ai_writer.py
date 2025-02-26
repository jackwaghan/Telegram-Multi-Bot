from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
import openai
from config import writer_id
from utils import text_menu_message
from keyboards import main_menu
from keyboards import ai_writer as ai_writer_keyboards

WRITER = 5 # Define the state

async def ai_writer(update: Updater, context: CallbackContext) -> int:
    """Display the AI Writer menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="Hello! I am a bot that integrates with the OpenAI GPT-3 and Built in Text to Speech API. You can ask me any question and I will try to provide a response.",
        reply_markup=ai_writer_keyboards.ai_writer_keyboard(),
    )
    return WRITER

async def writer(update: Updater, context: CallbackContext) -> int:
    """Write a response using OpenAI based on the user's input."""
    if update.effective_chat.id in writer_id:
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_writing..._",
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
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text=response["choices"][0]["text"],
            reply_markup=ai_writer_keyboards.ai_writer_per_keyboard(),
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

async def speech_to_text(update: Updater, context: CallbackContext) -> int:
    """Display the Speech to Text menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🎙️ Send me the audio file you want to convert to text.",
        reply_markup=ai_writer_keyboards.speech_to_text_keyboard(),
    )
    return SPEECH_TO_TEXT

async def speech_to_text_file(update: Updater, context: CallbackContext) -> int:
    """Convert the given audio file to text using Google Cloud Speech-to-Text API."""
    try:
        # Check if audio.mp3 exists and remove it
        if os.path.exists("audio.mp3"):
            os.remove("audio.mp3")

        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_Converting..._",
            parse_mode=ParseMode.MARKDOWN,
        )
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "telegram-375311-ee596015f2e9.json"
        speech_client = speech.SpeechClient()

        # Download the audio file
        media_file_name_mp3 = await update.message.audio.get_file().download(
            custom_path="audio.mp3"
        )

        with open("audio.mp3", "rb") as f1:
            byte_data_mp3 = f1.read()
        audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

        # Configure Media Files Output
        config_mp3 = speech.RecognitionConfig(
            sample_rate_hertz=48000,
            enable_automatic_punctuation=True,
            language_code="en-US",
        )

        # Transcribing the RecognitionAudio objects
        response_standard_mp3 = speech_client.recognize(config=config_mp3, audio=audio_mp3)

        text = response_standard_mp3.results[0].alternatives[0].transcript
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="{}".format(text),
            reply_markup=ai_writer_keyboards.speech_to_text_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value

    except Exception as e:
        print(f"Speech-to-text error: {e}")  # Log the error
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="❌ Error! Please send me a valid audio file.",
            reply_markup=ai_writer_keyboards.speech_to_text_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value

async def web_scrape(update: Updater, context: CallbackContext) -> int:
    """Display the Web Scraping menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="🔎 Send me the website you want to scrape.",
        reply_markup=ai_writer_keyboards.web_scrape_keyboard(),
    )
    return WEB_SCRAPE

async def web_scarpe_file(update: Updater, context: CallbackContext) -> int:
    """Scrape the given website and send the HTML file."""
    try:
        # Check if web_scrape.html exists and remove it
        if os.path.exists("web_scrape.html"):
            os.remove("web_scrape.html")

        global message
        # Make a request to the website
        message = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_Scraping..._",
            parse_mode=ParseMode.MARKDOWN,
        )

        url = "{}".format(update.message.text)
        response = requests.get(url)

        # Extract the HTML
        html = response.text

        # Search the HTML for CSS and JavaScript links
        css_links = []
        js_links = []

        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("link"):
            if link.get("href") and link.get("href").endswith(".css"):
                css_links.append(link.get("href"))

        for script in soup.find_all("script"):
            if script.get("src") and script.get("src").endswith(".js"):
                js_links.append(script.get("src"))

        # Download the HTML file
        with open("web_scrape.html", "w", encoding="utf-8") as file:
            file.write(html)
        # Send the HTML file
        await context.bot.send_document(
            chat_id=update.effective_chat.id, document=open("web_scrape.html", "rb")
        )

        # delete the message
        await context.bot.delete_message(
            chat_id=update.effective_chat.id, message_id=message.message_id
        )

        # send the message
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="📄 Here is the HTML file of the website you requested.",
            reply_markup=ai_writer_keyboards.web_scrape_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value

    except Exception as e:
        print(f"Web scraping error: {e}")  # Log the error
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=message.message_id,
            text="❌ Error! Please send me a valid website.",
            reply_markup=ai_writer_keyboards.web_scrape_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value