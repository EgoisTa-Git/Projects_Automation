import json
import random
from faker import Faker


def generate_listener(number):
    # генерим ученика
    listener_cards = []
    for _ in range(number):
        listener = f'"name": "{fake.name()}"'
        level = f'"level": "{user_levels[random.randint(0, 2)]}"'
        tg_username = f'"tg_username": "@{listener[9:-1].replace(" ", "")}"'
        discord_username = f'"discord_username": "{listener[9:-1].replace(" ", "")}#{random.randint(1000, 9999)}"'
        is_far_east = f'"is_far_east": "{bool(random.randint(0, 1))}"'
        listener_card_str = "{" + f'{listener}, {level}, {tg_username}, {discord_username}, {is_far_east}' + "}"
        # переводим карточку участника из строки в словарь и добавляем к списку
        listener_cards.append(json.loads(listener_card_str))
    return listener_cards


fake = Faker()
number = (int(input("Введите необходимое число учеников: ")))
user_levels = ['junior', 'novice+', 'novice']
listener_cards = generate_listener(number)
