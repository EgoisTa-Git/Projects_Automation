import pm_json_generator


def reading_pm_json():
    for pm_card in pm_json_generator.pm_cards:
        pm_info = (pm_card["name"], pm_card["start_time"], pm_card["end_time"], pm_card["tg_pmname"])
        yield pm_info


reading_pm_json()