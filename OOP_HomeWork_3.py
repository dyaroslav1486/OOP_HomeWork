class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_all = 0
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
        average_count = 0
        for course in self.courses_in_progress:
            if course in self.grades:
                summary_grades = sum(self.grades[course])
                average_grade = round(summary_grades/len(self.grades[course]),1)
                print(f"Средняя оценка за курс {course} = {average_grade}")
                sum_average += average_grade
                average_count += 1
            else:
                print(f"Нет оценок за курс {course}")
        self.average_grade_all = round(sum_average/average_count,1)
        print(f"Средняя оценка за домашние задания: {self.average_grade_all} ")
        print(f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}")
        return f"Завершенные курсы: {", ".join(self.finished_courses)}"
    
    def __lt__(self, other):
        return self.average_grade_all < other.average_grade_all
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade_all = 0

    def __str__(self):
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        sum_average = 0
        average_count = 0
        for course in self.courses_attached:
            if course in self.grades:
                summary_grades = sum(self.grades[course])
                average_grade = round(summary_grades/len(self.grades[course]),1)
                print(f"Средняя оценка за курс {course} = {average_grade}")
                sum_average += average_grade
                average_count += 1
            else:
                print(f"Нет оценок за курс {course}")
        self.average_grade_all = {round(sum_average/average_count,1)}
        return (f"Средняя оценка за лекции: {self.average_grade_all} ")
    
    def __lt__(self, other):
        return self.average_grade_all < other.average_grade_all


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
lecturer_2 = Lecturer('Петр', 'Петров')
reviewer = Reviewer('Пётр', 'Петров')
student_2 = Student('Алёхина', 'Ольга', 'Допельгангер')
student = Student('Ольга', 'Алехина', 'Ж')
 

student.courses_in_progress += ['Python', 'C++']
student_2.courses_in_progress += ['Python', 'C++']
student.finished_courses += ['Java']
lecturer.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python', 'C++']
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
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "Python", 2)

reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)

print(student)
print(student_2)
print(f"Ольга лучше своего доппельгангера? {student > student_2}")
print(lecturer)
print(lecturer_2)
print(f"Новый преподаватель лучше старого? {lecturer > lecturer_2}")
print(reviewer)