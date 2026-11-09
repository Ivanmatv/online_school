from users_data import users_dict
from user import User


class Teacher(User):
    def __init__(self, name: str):
        super().__init__(name)
        self.__name = name

    def teach(self, students: list, course_name: str) -> None:
        students_list = ', '.join(students)
        print(f"{self.__name} провёл урок {course_name}для учеников: {students_list}")

        for student_name in students_list:
            student = users_dict[student_name]
            student.study()
