from user import User


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__name = name
        self.__courses = dict()

    def get_courses(self) -> list:
        courses_length = len(self.__courses)
        if courses_length == 0:
            print("Студент не записан на курсы")

        print(f"Курсы студента {self.__name}")
        for teacher, course in self.__courses.items():
            print(f"{teacher} - {course}")

    def add_course(self, teacher: str, course: str) -> None:
        if teacher in self.__courses:
            self.__courses[teacher] = course

        self.__courses[teacher] = course
