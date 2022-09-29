def read_students_data(data):
    for student in data:
        name = student['name']
        tg_username = student['tg_username']
        level = student['level']
        yield name, tg_username, level


def read_managers_data(data):
    for manager in data:
        name = manager['name']
        tg_username = manager['tg_username']
        preferred_time = manager['preferred_time']
        yield name, tg_username, preferred_time
