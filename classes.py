import datetime


class Student:
    registry = []

    def __init__(self, name, tg_username, level):
        self.registry.append(self)
        self.name = name
        self.username = tg_username
        self.level = level
        self.vote_passed = False
        self.last_vote_date = datetime.datetime.now()
        self.preferred_start_time = datetime.time(
            hour=19,
            minute=30,
        ).isoformat(timespec='minutes')
        self.preferred_end_time = datetime.time(
            hour=21,
            minute=00,
        ).isoformat(timespec='minutes')

    def __str__(self):
        return f'{self.name}, {self.username}, level: {self.level}'


class Manager:
    def __init__(self, name, tg_username):
        self.name = name
        self.username = tg_username
        self.preferred_start_time = datetime.time(
            hour=19,
            minute=30,
        ).isoformat(timespec='minutes')
        self.preferred_end_time = datetime.time(
            hour=21,
            minute=00,
        ).isoformat(timespec='minutes')

    def __str__(self):
        return f'{self.name}, {self.username}'


student = Student('Сергей', '@student', 'novice')
print('Всего студентов:', len(Student.registry))
print(student)
print('готов к созвону в', student.preferred_start_time)
manager = Manager('Тим', '@manager')
print(manager)
