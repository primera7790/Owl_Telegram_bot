import telebot
from telebot.types import Message
import os
from dotenv import load_dotenv
import random

load_dotenv('./data/env/.env')

TOKEN = os.environ.get('O_TOKEN')
bot = telebot.TeleBot(TOKEN)


def else_answer(message):
    with open('num_incorrect_request.txt') as f:
        num_incorrect_request = f.read()
    if int(num_incorrect_request) == 2:
        bot.send_message(message.from_user.id, 'Это всё, конечно, занятно.. но вопрос-то поступит?)')
        with open('num_incorrect_request.txt', 'w') as f:
            f.write(str(0))
    else:
        with open('num_incorrect_request.txt', 'w') as f:
            f.write(str(int(num_incorrect_request) + 1))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Какой вопрос привёл тебя ко мне?')


@bot.message_handler(content_types=[
    'text',
    'audio',
    'document',
    'photo',
    'sticker',
    'video',
    'video_note',
    'voice',
    'location',
    'contact',
    'new_chat_members',
    'left_chat_member',
    'new_chat_title',
    'new_chat_photo',
    'delete_chat_photo',
    'group_chat_created',
    'supergroup_chat_created',
    'channel_chat_created',
    'migrate_to_chat_id',
    'migrate_from_chat_id',
    'pinned_message'
])
def echo_all(message: Message):
    if message.content_type == 'text':
        if len(message.text) > 3:

            questions_key_words = {
                'согласен': 'Согласен!',
                'правильно': 'Правильно!',
                'поддерживаешь': 'Поддерживаю!'
            }
            answers = [
                'Угу',
                'Так и есть!',
                'Не поспоришь',
                'Конечно!',
                'А как иначе',
                'Агась',
                'А кто-то думает иначе??',
                'ОО, да!',
                'Угу',
                'Безусловно',
                'Вот тут я, пожалуй, отмолчусь..',
                'Главное, что ты в это веришь!',
                'Скажешь тоже..',
                'Угу'
            ]
            cycles = 0
            for i in questions_key_words:
                if message.text.lower().find(i) > -1:
                    bot.send_message(message.from_user.id, questions_key_words[i])
                else:
                    cycles += 1
                if cycles == len(questions_key_words):
                    bot.send_message(message.from_user.id, random.choice(answers))

            with open('num_incorrect_request.txt', 'w') as f:
                f.write(str(0))
                f.close()

        else:
            else_answer(message)
    else:
        else_answer(message)


bot.infinity_polling()
