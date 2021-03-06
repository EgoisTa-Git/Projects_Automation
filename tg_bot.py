import json
import os

import telebot
from dotenv import load_dotenv
from telebot import types

from classes import Student, Manager
from filters import find_vacant_manager, add_student_to_group
from filters import get_student, get_timetable
from json_reader import read_students_data, read_managers_data

load_dotenv()
TG_API_KEY = os.getenv('TG_BOT_API_KEY')
bot = telebot.TeleBot(TG_API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    username = f'@{message.from_user.username}'
    for user in Student.registry:
        if username == user.username and not user.vote_passed:
            get_time(message, user)
            return
        elif username == user.username and user.vote_passed:
            bot.send_message(
                message.chat.id,
                f'Привет, {user.name}.\n Ты записан(а) на'
                f' {user.preferred_start_time}:00'
            )
            return
    for user in Manager.registry:
        if username == user.username:
            bot.send_message(
                message.chat.id,
                f'Привет, {user.name}'
            )
            bot.send_message(
                message.chat.id,
                get_timetable(user)
            )
            return
    bot.send_message(
        message.chat.id,
        'Привет, гость. Хочешь в IT? Тогда тебе сюда: dvmn.org'
    )


def get_time(message, user):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    global available_time
    start_time = 24
    end_time = 0
    for manager in Manager.registry:
        if manager.preferred_start_time < start_time:
            start_time = manager.preferred_start_time
        if manager.preferred_end_time > end_time:
            end_time = manager.preferred_end_time
    for time_ in range(start_time, end_time):
        button = types.KeyboardButton(f'{time_}:00-{time_+1}:00')
        markup.add(button)
        available_time.append(f'{time_}:00-{time_+1}:00')
    bot.send_message(
        message.chat.id,
        f'Привет, {user.name}. Выбери удобное время для созвона:',
        reply_markup=markup,
    )


@bot.message_handler(content_types=['text'])
def select_time(message):
    if message.text in available_time:
        answer = message.text
    else:
        bot.send_message(
            message.chat.id,
            'Необходимо выбрать время',
        )
        return
    bot.send_message(
        message.chat.id,
        f'Вы выбрали {answer}',
        reply_markup=types.ReplyKeyboardRemove(),
    )
    username = f'@{message.from_user.username}'
    user = get_student(username)
    time_ = int(answer[:2])
    vacant_manager = find_vacant_manager(time_, user)
    if vacant_manager:
        add_student_to_group(vacant_manager, time_, user)
    else:
        bot.send_message(
            message.chat.id,
            'Время уже занято. Необходимо выбрать другое время.',
        )
        start(message)


if __name__ == '__main__':
    available_time = []
    with open('students.json', 'r') as file:
        students_data = json.loads(file.read())
    with open('managers.json', 'r') as file:
        managers_data = json.loads(file.read())
    for name, tg_username, level in read_students_data(students_data):
        student = Student(name, tg_username, level)
    for name, tg_username, preferred_time in read_managers_data(managers_data):
        manager = Manager(name, tg_username, preferred_time)
    bot.polling(none_stop=True)
