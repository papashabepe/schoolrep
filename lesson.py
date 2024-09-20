class Lesson:
    def __init__(self, subject , classroom , time):
        self.__subject = subject
        self.__classroom = classroom
        self.__time = time

    def __str__(self):
        return "|" + self.__time + "|" + self.__subject + "|" + self.__classroom + "|"