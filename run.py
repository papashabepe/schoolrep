from calendar import weekday

from constans import SUBJECT, CLASSROOMS , TIME
from lesson import Lesson
from school_day import SchoolDay

lesson = Lesson(SUBJECT[0] , CLASSROOMS[0] ,TIME[0])
weekday = SchoolDay("Monday")
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
weekday.appendLesson(lesson)
print(weekday)
