import json
import random
from faker import Faker


def generate_pm():
    # генерим ПМа
    pm_cards = []
    number = (int(input("Введите необходимое число ПМов: ")))
    for _ in range(number):
        start_time = random.randint(18, 24)
        end_time = random.randint(start_time, 24)

        pm = f'"name": "{fake.name()}"'
        possible_start_time = f'"start_time": {start_time}'
        possible_end_time = f'"end_time": {end_time}'
        tg_pmname = f'"tg_pmname": "@{pm[9:-1].replace(" ", "")}"'
        discord_pmname = f'"discord_pmname": "{pm[9:-1].replace(" ", "")}#{random.randint(1000, 9999)}"'

        pm_card_str = "{" + f'{pm}, {possible_start_time}, {possible_end_time}, {tg_pmname}, {discord_pmname}' + "}"
        # переводим карточку ПМа из строки в словарь и добавляем к списку
        pm_cards.append(json.loads(pm_card_str))
    return pm_cards


fake = Faker()
pm_cards = generate_pm()