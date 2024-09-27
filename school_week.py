class SchoolWeek:
        def __init__(self):
            self.__days = dict()

        def addDay(self , day , day_of_week):
            self.__days[day_of_week] = day

        def __str__(self):
            school_week = str()
            for day in self.__days:
                school_week += day + '\n'
                school_week += self.__days[day].__str__() + '\n'

            return school_week