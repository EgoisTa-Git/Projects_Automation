import json

from json_reader import read_students_data, read_managers_data


class Student:
    registry = []

    def __init__(self, name, tg_username, level):
        self.name = name
        self.username = tg_username
        self.level = level
        self.vote_passed = False
        self.preferred_start_time = 0
        self.preferred_end_time = 0
        self.registry.append(self)

    def __str__(self):
        return f'{self.name}, {self.username}, level: {self.level}'


class Manager:
    registry = []

    def __init__(self, name, tg_username, preferred_time):
        self.name = name
        self.username = tg_username
        self.preferred_time = preferred_time.split(':00')
        self.preferred_start_time = abs(int(self.preferred_time[0]))
        self.preferred_end_time = abs(int(self.preferred_time[1]))
        self.registry.append(self)

    def __str__(self):
        return f'{self.name}, {self.username}'


if __name__ == '__main__':
    with open('students.json', 'r') as file:
        students_data = json.loads(file.read())
    with open('managers.json', 'r') as file:
        managers_data = json.loads(file.read())
    for name, tg_username, level in read_students_data(students_data):
        student = Student(name, tg_username, level)
    for name, tg_username, preferred_time in read_managers_data(managers_data):
        manager = Manager(name, tg_username, preferred_time)

    for student in Student.registry:
        print(student)
    for manager in Manager.registry:
        print(manager)
