from teacher import Teacher
from user import User


class Student(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__name = name

    def study(self, teacher: Teacher) -> None:
        teacher_name = teacher.get_name()
        print(f"{self.__name} учиться у {teacher_name}")
