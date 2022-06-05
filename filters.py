from classes import Student, Manager


def find_vacant_manager(time_, user):
    for manager in Manager.registry:
        for vacant_time, students in manager.timetable.items():
            if 1 <= len(students) < 3:
                if time_ == vacant_time and students[0].level == user.level:
                    return manager
            elif not students:
                if time_ == vacant_time:
                    return manager


def add_student_to_group(manager, time_, user):
    manager.timetable[time_].append(user)
    user.vote_passed = True
    user.preferred_start_time = time_


def get_student(username):
    for user in Student.registry:
        if username == user.username:
            return user
