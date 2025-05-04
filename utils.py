import config

def parse_message(message):
    text = message["message"]["text"].lower()
    chat_id = message["message"]["from"]["id"]   
    return [text,chat_id]

def parse_description(text):
    new_text = text.replace(" ","+").replace(",","+")
    new_text = new_text.replace("++","+")
    return new_text

def parse_callback(message):
    text = message['callback_query']['data']
    chat_id = message['callback_query']['message']['chat']['id']
    return[text,chat_id]

def check_callback_query(text_callback):

    if text_callback == "Влево":
        if config.img_actual == 1:
            if config.page_actual == 1:
                config.page_actual = config.max_pages
            else:
                config.page_actual -= 1
            config.img_actual = config.per_page
        else:
            config.img_actual -= 1
    else: 
        if text_callback == "Вправо":
            if config.img_actual == config.per_page:
                config.img_actual = 1
                if config.page_actual == config.max_pages:
                    config.page_actual = 1
                else:
                    config.page_actual += 1
            else:
                config.img_actual += 1