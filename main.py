from student import Student
from teacher import Teacher


student_ivan = Student(name="Ваня", user_type="student")
student_igor = Student(name="Игорь", user_type="student")

teacher_math = Teacher(name="Виктор", user_type="teacher")
teacher_prog = Teacher(name="Стас", user_type="teacher")

math_course = 'Математика'
prog_course = 'Программирование'

teacher_prog.create_course(prog_course)
teacher_math.create_course(math_course)

users = [student_ivan, student_igor, teacher_math, teacher_prog]

for user in users:
    user_type = user.get_type()
    if user_type == "student":
        teacher_math.add_student(math_course, user)


teacher_math.show_courses()

print()

teacher_math.show_students(math_course)