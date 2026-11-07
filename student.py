from teacher import Teacher
from user import User


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__name = name

    def study(self) -> None:
        print(f"Студент {self.__name} был на уроке")
