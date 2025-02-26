from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater
from email.mime.text import MIMEText
import smtplib
from config import bot_link
from keyboards import ai_mail as ai_mail_keyboards

MAIL = 0 # Define the state
TO = 3 # Define the state
MESSAGE = 4 # Define the state

async def mail(update: Updater, context: CallbackContext) -> int:
    """Display the mail menu."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="📧 Send me the email address you want to send the email to.",
        reply_markup=ai_mail_keyboards.mail_keyboard(),
    )
    return TO

async def to(update: Updater, context: CallbackContext) -> int:
    """Get the recipient's email address."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Message"
    )
    to_email = update.message.text
    open("to.txt", "w").write(to_email)
    return MESSAGE

async def message(update: Updater, context: CallbackContext) -> int:
    """Send the email message."""
    try:
        txt = open("to.txt", "r").read()
        message_text = update.message.text
        msg = MIMEText("{}\n\nFrom AI-Robot\n{}".format(message_text, bot_link))
        msg["Subject"] = "AI-Robot"
        msg["From"] = "admin@jackwaghan.ml"
        msg["To"] = "{}".format(txt)
        send = await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="_sending..._",
            parse_mode=ParseMode.MARKDOWN,
        )
        sender_email = "admin@jackwaghan.ml"
        receiver_email = "{}".format(txt)
        password = "5e61423ab9ca47bcaa84a2efc76c1a88-f7d687c0-4f8f8c63"

        message = msg.as_string()
        server = smtplib.SMTP("smtp.mailgun.org", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        await context.bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=send.message_id,
            text="📬check your Inbox",
            reply_markup=ai_mail_keyboards.ai_mail_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value
    except Exception as e:
        print(f"Mail error: {e}")  # Log the error
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="❌ Something went wrong, please provide a valid email address.",
            reply_markup=ai_mail_keyboards.ai_mail_per_keyboard(),
        )
        return 0 # Replace CALLBACK with the actual value