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
