class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        sum_average = 0
        for course in self.courses_in_progress:
            if course in self.grades:
                summary_grades = sum(self.grades[course])
                average_grade = round(summary_grades/len(self.grades[course]),1)
                print(f"Средняя оценка за курс {course} = {average_grade}")
                sum_average += average_grade
            else:
                print(f"Нет оценок за курс {course}")
        print(f"Средняя оценка за домашние задания: {round(sum_average/len(self.courses_in_progress),1)} ")
        print(f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}")
        return f"Завершенные курсы: {", ".join(self.finished_courses)}"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        sum_average = 0
        for course in self.courses_attached:
            if course in self.grades:
                summary_grades = sum(self.grades[course])
                average_grade = round(summary_grades/len(self.grades[course]),1)
                print(f"Средняя оценка за курс {course} = {average_grade}")
                sum_average += average_grade
            else:
                print(f"Нет оценок за курс {course}")
        return (f"Средняя оценка за лекции: {round(sum_average/len(self.courses_attached),1)} ")

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        print(f"Имя: {self.name}")
        return f"Фамилия: {self.surname}"
        
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
 
student.courses_in_progress += ['Python', 'C++']
student.finished_courses += ['Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'C++', 7)
reviewer.rate_hw(student, 'Python', 6)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'C++', 7)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'C++', 2)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "Python", 10)
student.rate_lecture(lecturer, "Python", 8)
student.rate_lecture(lecturer, "Python", 10)

print(student)
print(lecturer)
print(reviewer)