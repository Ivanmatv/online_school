from user import User


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__name = name

    def teach(self, students: list) -> None:
        students_list = ', '.join(students)
        print(f"{self.__name} провёл урок для учеников: {students_list}")

