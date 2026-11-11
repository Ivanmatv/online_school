from course import Course
from student import Student
from users_data import users, courses


def show_students() -> None:
    print("Студенты:")
    for user_name, user_type in users.items():
        if isinstance(user_type, Student):
            print(f'- {user_name}')

def show_courses() -> None:
    print("Курсы:")
    for course_name, course_type in courses.items():
        course_teacher = course_type.get_teacher()
        teacher_name = course_teacher.get_name()
        print(f'Учитель {teacher_name} - {course_name}')

def show_course_students(course: Course) -> None:
    course_name = course.get_name()
    course_teacher = course.get_teacher()
    teacher_name = course_teacher.get_name()
    student_list = course.get_students()
    formatted_student_list = ", ".join(student_list)

    print(
        f"На курс {teacher_name} - {course_name}\n"
        f"Записаны студенты: {formatted_student_list}"
    )

def course_enrollment():
    show_students()
    print()
    show_courses()

    course = ''

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

                is_student = users.get(chosen_student, "")
                if chosen_student not in users or not isinstance(is_student, Student):
                    chosen_student = False
                    print("Нет такого студента")

            chosen_course = ""
            while not chosen_course:
                chosen_course = input("Введите название курса: ").strip()

                course_list = [course_type.get_name() for _ ,course_type in courses.items()]
                if chosen_course not in course_list:
                    chosen_course = False
                    print("Нет такого курса")

            student = users[chosen_student]
            course = courses[chosen_course]
            if isinstance(student, Student):
                course.add_student(student=student)

            show_course_students(course)

    return course


def main():
    course = course_enrollment()

    print("\nСтуденты записались на курсы\n")

    course_name = course.get_name()
    students= course.get_students()
    teacher = course.get_teacher()
    teacher.teach(students=students, course_name=course_name)

main()
