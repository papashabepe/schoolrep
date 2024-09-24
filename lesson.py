


class Lesson:
    def __init__(self ,week_days ,  subject , classroom , time):
        self.__subject = subject
        self.__classroom = classroom
        self.__time = time
        self.__week_days = week_days
    def __str__(self):
            return "|"+ self.__week_days + "|" + self.__time + "|" + self.__subject + "|" + self.__classroom + "|"