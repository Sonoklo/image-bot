from bot_controller import send_message

def start_handler(chat_id):
    send_message(chat_id,"Добро пожаловать в бота\n Напишите описания картинки что бы ее получить")