from calendar import weekday

from constans import SUBJECT, CLASSROOMS, TIME, WEEK_DAYS
from lesson import Lesson
from school_day import SchoolDay
from school_week import SchoolWeek

lesson = Lesson(WEEK_DAYS[0] , SUBJECT[0] , CLASSROOMS[0] ,TIME[0])
weekday = SchoolDay()
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.__str__()
school_week = SchoolWeek()
school_week.addDay(weekday , WEEK_DAYS[0])
school_week.addDay(weekday , WEEK_DAYS[1])
school_week.addDay(weekday , WEEK_DAYS[2])
school_week.addDay(weekday , WEEK_DAYS[3])
school_week.addDay(weekday , WEEK_DAYS[4])
print(school_week)