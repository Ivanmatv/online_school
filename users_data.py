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

unique_users = {student_ivan, student_igor, mathematics_teacher, programming_teacher}
users = dict()

for user in unique_users:
    user_name = user.get_name()
    users[user_name] = user

mathematics_course = Course(name='Математика', teacher=mathematics_teacher)
programming_course = Course(name='Программирование', teacher=programming_teacher)

unique_courses = [mathematics_course, programming_course]
courses = dict()

for course in unique_courses:
    course_name = course.get_name()
    courses[course_name] = course
