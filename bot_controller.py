import requests
import config
import json
from utils import parse_description,check_callback_query

def get_message():
    params = {"offset": config.offset}
    resp = requests.get(f"https://api.telegram.org/{config.TOKEN_BOT}/getUpdates", params = params)
    data = resp.json()
    return data["result"]

def send_message(chat_id, text, keyboard=None):
    params = {"chat_id": chat_id, "text": text}
    if keyboard:
        params["reply_markup"] = json.dumps(keyboard)

    requests.get(f"https://api.telegram.org/{config.TOKEN_BOT}/sendMessage", params=params)

def get_image(text):
    params = {"key": config.TOKEN_PIXABAY, "q": parse_description(text), "page": config.page_actual, "per_page": config.per_page}
    resp = requests.get(f"https://pixabay.com/api/", params)
    data = resp.json()
    return data


def send_image_and_description(chat_id, text, text_callback=None):
    
    if text_callback is not None:
        check_callback_query(text_callback)

    keyboard = {
        "inline_keyboard":[
            [{"text": "Влево", "callback_data": "Влево"},{"text": "Вправо", "callback_data": "Вправо"}]
        ]
    }
    data = get_image(text)

    if data["total"] > 0:
        config.max_pages = data["totalHits"] // config.per_page
        image_url = data["hits"][config.img_actual - 1]["webformatURL"]
        
        params = {"chat_id": chat_id, "photo": image_url, "caption":text}
        params["reply_markup"] = json.dumps(keyboard)
        requests.get(f"https://api.telegram.org/{config.TOKEN_BOT}/sendPhoto", params=params)
    else:
        send_message(chat_id,"Картинка не была найдена")

def get_caption():
    params = {"offset": config.offset}
    resp = requests.get(f"https://api.telegram.org/{config.TOKEN_BOT}/getUpdates", params = params)
    data = resp.json()
    caption = data["result"][0]["callback_query"]["message"]["caption"]
    return caption