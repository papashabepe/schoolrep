from calendar import weekday

from lesson import Lesson


class SchoolDay:
    def __init__(self):
        self.__lessons = []

    def appendLesson(self , lesson):
        self.__lessons.append(lesson)

    def __str__(self):
        weekday = str()
        for lesson in self.__lessons:
            weekday += lesson.__str__() + "\n"

        return weekday