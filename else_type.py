import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('O_TOKEN')
bot = telebot.TeleBot(TOKEN)


def else_type(message):
    with open('num_incorrect_request.txt', 'r') as f:
        num_incorrect_request = f.read()
    if int(num_incorrect_request) == 2:
        bot.send_message(message.from_user.id, 'Это всё, конечно, занятно.. но вопрос-то поступит?)')
        with open('num_incorrect_request.txt', 'w') as f:
            f.write(str(0))
            f.close()
    else:
        with open('num_incorrect_request.txt', 'w') as f:
            f.write(str(int(num_incorrect_request) + 1))
            f.close()