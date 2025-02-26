import json

def load_config():
    with open('keys.json') as f:
        key_data = json.load(f)
        key = key_data['hash_key']
        open_ai_key = key_data['openai_key']
        contact = key_data['contact']
        donate = key_data['donate']
        bot_link = key_data['bot_link']
        bot_token = key_data['bot_token']

    with open("chat.json") as g:
        chat_data = json.load(g)
        capture_id = chat_data['capture_id']
        listener_id = chat_data['listener_id']
        writer_id = chat_data['writer_id']
        reader_id = chat_data['reader_id']

    return {
        'key': key,
        'open_ai_key': open_ai_key,
        'contact': contact,
        'donate': donate,
        'bot_link': bot_link,
        'bot_token': bot_token,
        'capture_id': capture_id,
        'listener_id': listener_id,
        'writer_id': writer_id,
        'reader_id': reader_id
    }

config = load_config()
key = config['key']
open_ai_key = config['open_ai_key']
contact = config['contact']
donate = config['donate']
bot_link = config['bot_link']
bot_token = config['bot_token']
capture_id = config['capture_id']
listener_id = config['listener_id']
writer_id = config['writer_id']
reader_id = config['reader_id']