from student import Student
from teacher import Teacher


class Course:
    def __init__(self, name: str, teacher: Teacher) -> None:
        self.__name = name
        self.__students = set()
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

    def get_name(self) -> str:
        return self.__name

    def add_student(self, student: Student) -> None:
        if student not in self.__students:
            self.__students.add(student)
        else:
            print("Студен уже записан на курс.")

    def get_students(self) -> list:
        return [student.get_name() for student in self.__students]

    def remove_student(self, student: Student, teacher: Teacher) -> None:
        if student not in self.__students:
            print("Такого студента нет в списке")
        else:
            self.__students.remove(student)
