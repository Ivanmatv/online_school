from student import Student
from user import User


class Teacher(User):
    def __init__(self, name: str, user_type: str):
        super().__init__(name, user_type)
        self.__name = name
        self.__user_type = user_type
        self.__courses = dict()

    def create_course(self, course: str) -> None:
        if course not in self.__courses:
            self.__courses[course] = list()
        else:
            print("Такой курс уже есть!")

    def show_courses(self) -> None:
        length_courses = len(self.__courses)
        empty_courses = 0

        if length_courses != empty_courses:
            print(f'Курсы преподавателя {self.__name}:')
            for course in self.__courses:
                print(f'- {course}')
        else:
            print("Курсов нет!")

    def remove_course(self, course: str) -> None:
        if course not in self.__courses:
            del self.__courses[course]
        else:
            print("Такого курса нет!")

    def add_student(self, course: str, student: Student) -> None:
        if course not in self.__courses:
            print("Такого курса нет!")

        if student not in self.__courses[course]:
            self.__courses[course].append(student)

    def show_students(self, course: str) -> None:
        if course in self.__courses:
            students = self.__courses[course]
            print(f"Студенты {self.__name} - курса {course}:")

            for student in students:
                student_name = student.get_name()
                print(f'- {student_name}')
        else:
            print("Такого курса нет!")

    def remove_student(self, course: str, student: str) -> None:
        if course not in self.__courses:
            print("Такого курса нет!")

        if student not in self.__courses[course]:
            self.__courses[course].remove(student)
