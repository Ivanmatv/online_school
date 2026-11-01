from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__course = dict()

    def add_teacher(self, teacher: Teacher) -> None:
        if teacher not in self.__course:
            self.__course[teacher] = list()
        else:
            print("Преподаватель уже ведёт курс")

    def add_student(self, student: Student, teacher: Teacher) -> None:
        if teacher not in self.__course:
            print("Такой учитель не ведёт курс")

        if student not in self.__course[self.__name]:
            self.__course[teacher].append(student)

    def show_students(self, teacher: Teacher) -> None:
        students = self.__course[teacher]
        formatted_students_list = ', '.join(students)

        print(f"Студенты преподавателя {teacher} - курса {self.__name}:")
        print(formatted_students_list)

    def remove_student(self, student: Student, teacher: Teacher) -> None:
        if student not in self.__course[teacher]:
            print("Такого студента нет в списке")

        self.__course[self.__name].remove(student)
