import json
import random
from faker import Faker

STUDENTS = 40
MANAGERS = 3


def create_student():
    levels = ['junior', 'novice+', 'novice']
    name = fake.name()
    tg_username = f'@{name.replace(" ", "")}'
    level = random.choice(levels)
    discord_username = f'{name.replace(" ", "")}#{random.randint(1000, 9999)}'
    is_far_east = bool(random.randint(0, 1))
    return {
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
    return {
        'name': name,
        'tg_username': tg_username,
        'discord_username': discord_username,
        'preferred_time': preferred_time,
    }


if __name__ == '__main__':
    fake = Faker()
    students = []
    managers = []
    for _ in range(STUDENTS):
        students.append(create_student())
    with open('students.json', 'w') as file:
        file.write(json.dumps(students, skipkeys=True))
    for _ in range(MANAGERS):
        managers.append(create_pm())
    with open('managers.json', 'w') as file:
        file.write(json.dumps(managers, skipkeys=True))
