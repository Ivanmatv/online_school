from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str, teacher: str) -> None:
        self.__name = name
        self.__course = dict()
        self.__teacher = teacher
        self.add_teacher()

    def add_teacher(self):
        self.__course[self.__teacher] = list()

    def get_name(self) -> str:
        return self.__name

    def add_student(self, student: Student) -> None:
        if student not in self.__course[self.__teacher]:
            self.__course[self.__teacher].append(student)
        else:
            print("Студен уже записан на курс.")

    def get_students(self) -> list:
        return [student.get_name() for student in self.__course[self.__teacher]]

    def remove_student(self, student: Student, teacher: Teacher) -> None:
        if student not in self.__course[teacher]:
            print("Такого студента нет в списке")
        else:
            self.__course[self.__teacher].remove(student)

    def get_teacher(self):
        self.__course.keys()
        teacher = ' '.join(self.__course.keys())

        return teacher