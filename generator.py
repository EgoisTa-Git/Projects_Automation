import json
import random
from faker import Faker

STUDENTS = 40
MANAGERS = 3


def create_student():
    levels = ['junior', 'novice+', 'novice']
    name = fake.name()
    tg_username = f'@{name.replace(" ", "").lower()}'
    level = random.choice(levels)
    discord_username = f'{name.replace(" ", "")}#{random.randint(1000, 9999)}'
    is_far_east = random.choice([True, False])
    return tg_username, {
        'name': name,
        'level': level,
        'tg_username': tg_username,
        'discord_username': discord_username,
        'is_far_east': is_far_east,
    }


def create_pm():
    name = fake.name()
    tg_username = f'@{name.replace(" ", "").lower()}'
    discord_username = f'{name.replace(" ", "")}#{random.randint(1000, 9999)}'
    preferred_start_time = random.randint(18, 23)
    preferred_end_time = random.randint(preferred_start_time, 24)
    preferred_time = f'{preferred_start_time}:00-{preferred_end_time}:00'
    return tg_username, {
        'name': name,
        'tg_username': tg_username,
        'discord_username': discord_username,
        'preferred_time': preferred_time,
    }


if __name__ == '__main__':
    fake = Faker()
    students = {}
    managers = {}
    for _ in range(STUDENTS):
        student, attributes = create_student()
        students[student] = attributes
    with open('students_test.json', 'w') as file:
        file.write(json.dumps(students))
    for _ in range(MANAGERS):
        manager, attributes = create_pm()
        managers[manager] = attributes
    with open('managers_test.json', 'w') as file:
        file.write(json.dumps(managers))
