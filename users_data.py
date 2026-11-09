from course import Course
from student import Student
from teacher import Teacher


Ivan = "Иван"
Igor = "Игорь"
Viktor = "Виктор Михайлович"
Stas = "Станислав Владимирович"

student_ivan = Student(name=Ivan)
student_igor = Student(name=Igor)

mathematics_teacher = Teacher(name=Viktor)
programming_teacher = Teacher(name=Stas)

users = {student_ivan, student_igor, mathematics_teacher, programming_teacher}
users_dict = dict()

for user in users:
    user_name = user.get_name()
    users_dict[user_name] = user

mathematics_course = Course(name='Математика', teacher=mathematics_teacher)
programming_course = Course(name='Программирование', teacher=programming_teacher)

courses = [mathematics_course, programming_course]
courses_dict = dict()

for course in courses:
    course_name = course.get_name()
    courses_dict[course_name] = course
