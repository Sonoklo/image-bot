import config
import time 
from bot_controller import get_message, send_image_and_description,get_caption
from utils import parse_message,parse_callback
from handler_command import start_handler
if __name__ == "__main__":
    while True:
        for message in get_message():
            if "callback_query" in message:
                text_callback, chat_id = parse_callback(message)

                send_image_and_description(chat_id,get_caption(),text_callback)  
            
            else:
                text, chat_id = parse_message(message)
                
                if text == "/start":
                    start_handler(chat_id)
                
                elif type(text) is str:
                    send_image_and_description(chat_id, text)
            config.offset = message["update_id"] + 1
        time.sleep(1)