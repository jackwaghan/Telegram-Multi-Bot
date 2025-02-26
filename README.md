# Multi Bot ( AI )

This is a Telegram bot that provides various AI-powered tools, including:

- AI Writer
- AI Listener (Text to Speech)
- Web Capture
- URL Shortener
- Encryption/Decryption
- Speech to Text
- Web Scraping

## Prerequisites

- Python 3.7+
- Telegram Bot Token
- OpenAI API Key
- Google Cloud Speech-to-Text API Credentials (if using Speech to Text)
- Mailgun API Credentials (if using Mail)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd Telegram-Multi-Bot
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv myenv
    source myenv/scripts/activate  # On Linux/macOS
    myenv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**

    - Create a `keys.json` file with the following structure:

      ```json
      {
        "hash_key": "<your_hash_key>",
        "openai_key": "<your_openai_api_key>",
        "contact": "<your_contact_url>",
        "donate": "<your_donation_url>",
        "bot_link": "<your_bot_link>",
        "bot_token": "<your_telegram_bot_token>"
      }
      ```

    - Create a `chat.json` file with the following structure:

      ```json
      {
          "capture_id": [ <user_id_1>, <user_id_2> ],
          "listener_id": [ <user_id_1>, <user_id_2> ],
          "writer_id": [ <user_id_1>, <user_id_2> ],
          "reader_id": [ <user_id_1>, <user_id_2> ]
      }
      ```

      Replace `<user_id_1>`, `<user_id_2>`, etc., with the Telegram user IDs that have access to paid features.

    - If using the Speech to Text feature, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud Speech-to-Text API credentials file:

      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/google_credentials.json"  # Linux/macOS
      set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\google_credentials.json  # Windows
      ```

5.  **Run the bot:**

    ```bash
    python main.py
    ```

## Project Structure

- main.py

- Main entry point config.py

- Configuration loading utils.py

- Utility functions handlers/

- Telegram bot handlers init.py start.py ai_writer.py ai_listener.py ai_capture.py mail.py shortener.py encrypt_decrypt.py keyboards/

- Inline keyboard definitions init.py main_menu.py ai_writer.py ai_listener.py ai_capture.py ai_mail.py shortener.py encrypt_decrypt.py requirements.txt

- Python dependencies keys.json

- API keys and bot token chat.json

- Chat ID configuration README.md # This file

## API Keys and Credentials

- **Telegram Bot Token:** Obtain a bot token from BotFather on Telegram.

- **OpenAI API Key:** Get an API key from the OpenAI website.

- **Google Cloud Speech-to-Text API Credentials:** Create a service account and download the credentials file from the Google Cloud Console.

- **Mailgun API Credentials:** If using the mail functionality, you'll need to configure Mailgun and use your API key and domain.

**Important:** Store your API keys and credentials securely and do not commit them to your repository. Use environment variables or a secure configuration file.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License.
