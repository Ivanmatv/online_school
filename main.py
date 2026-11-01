from users_data import users
from student import Student
from teacher import Teacher

def main():
    print("Студенты:")
    for user, user_type in users.items():
        if isinstance(user_type, Student):
            print(f'- {user}')

    print()

    print("Преподаватели:")
    for user, user_class in users.items():
        if isinstance(user_class, Teacher):
            print(f'- {user}')
            courses = ','.join(user_class.get_courses())
            print(f"Курсы преподавателя: {courses}")

    STOP_COMMAND = "нет"
    input_command = ""

    while input_command != STOP_COMMAND:
        print()
        print("Выберите студента,"
              "которого хотите записать на курс.")
        print()

        input_command = input("Продолжить: Да или Нет - ").strip().lower()

        if input_command != STOP_COMMAND:
            chosen_student = ""
            while not chosen_student:
                chosen_student = input("Введите имя студента: ").strip()

                is_student = users[chosen_student]
                if chosen_student not in users or not isinstance(is_student, Student):
                    chosen_student = False
                    print("Нет такого студента")

            chosen_teacher = ""
            while not chosen_teacher:
                chosen_teacher = input("Введите имя преподавателя: ").strip()

                is_teacher = users[chosen_teacher]
                if chosen_teacher not in users or not isinstance(is_teacher, Teacher):
                    chosen_teacher = False
                    print("Нет такого преподавателя")

            teacher = users[chosen_teacher]
            courses = teacher.get_courses()

            for course in courses:
                print(f'- {course}')

            chosen_course = ""
            while not chosen_course:
                chosen_course = input("Выберите курс: ").strip()

                if chosen_course not in courses:
                    chosen_course = False
                    print("Нет такого курса")


            student = users[chosen_student]
            if isinstance(student, Student):
                teacher.add_student(course=chosen_course, student=student)

            teacher.show_students(chosen_course)

main()