import json
import student_cards


def reading_json():
    for student_card in student_cards.listener_cards:
        info = (student_card["name"], student_card["tg_username"], student_card["level"])
        yield info

reading_json()