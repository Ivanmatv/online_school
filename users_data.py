from student import Student
from teacher import Teacher

Ivan = "Иван"
Igor = "Игорь"
Viktor = "Виктор"
Stas = "Стас"

student_ivan = Student(name=Ivan)
student_igor = Student(name=Igor)

mathematics_teacher = Teacher(name=Viktor)
programming_teacher = Teacher(name=Stas)

mathematics_course = 'Математика'
programming_course = 'Программирование'

users = {
    Ivan : student_ivan,
    Igor : student_igor,
    Viktor : mathematics_teacher,
    Stas : programming_teacher,
}

programming_teacher.create_course(programming_course)
mathematics_teacher.create_course(mathematics_course)
