class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_all = 0
        all_students.append(self)
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
        if sum_average != 0:
            self.average_grade_all = round(sum_average/average_count,1)
        else:
            self.average_grade_all = 0
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
        all_Lecturer.append(self)

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
        if sum_average != 0:
            self.average_grade_all = round(sum_average/average_count,1)
        else:
            self.average_grade_all = 0
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
    
def average_course_grade_student(students, course):
    sum_grade_course = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress and course in student.grades:
            average_grade_student = round(sum(student.grades[course])/len(student.grades[course]), 1)
            sum_grade_course += average_grade_student
        else: 
            pass
    average_grade = round(sum_grade_course/len(students),1)
    return course, average_grade

def average_course_grade_lecturers(lecturers, course):
    sum_grade_course_lect = 0
    for lecturer in all_Lecturer:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.grades:
            average_grade_lecturer = round(sum(lecturer.grades[course])/len(lecturer.grades[course]), 1)
            sum_grade_course_lect += average_grade_lecturer
        else: 
            pass
    average_grade_lect = round(sum_grade_course_lect/len(all_Lecturer),1)
    return course, average_grade_lect

all_students = []
all_Lecturer = []
lecturer = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Петр', 'Петров')
reviewer = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Пётр', 'Иванов')
student_2 = Student('Алёхина', 'Ольга', 'Допельгангер')
student = Student('Ольга', 'Алехина', 'Ж')
student_3 = Student('ООльга', 'Алехина', 'Допельгангер')

 

student.courses_in_progress += ['Python', 'C++', 'Java']
student_2.courses_in_progress += ['Python', 'Java']
student_3.courses_in_progress += ['Python', 'C++',]
lecturer.courses_attached += ['Python', 'C++', 'Java']
lecturer_2.courses_attached += ['Python', 'Java']
reviewer.courses_attached += ['Python', 'C++', 'Java']
reviewer.courses_attached += ['Python', 'C++', 'Java']
 
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'C++', 7)
reviewer.rate_hw(student, 'Python', 6)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Java', 7)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student_3, 'Java', 10)
reviewer_2.rate_hw(student_3, 'Python', 4)
reviewer.rate_hw(student, 'C++', 2)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "Python", 10)
student.rate_lecture(lecturer, "Python", 8)
student.rate_lecture(lecturer, "Python", 10)
student.rate_lecture(lecturer, "Java", 9)
student.rate_lecture(lecturer, "Python", 9)
student.rate_lecture(lecturer, "C+=", 10)
student.rate_lecture(lecturer, "C++", 8)
student_2.rate_lecture(lecturer, "Java", 10)
student_2.rate_lecture(lecturer_2, "Java", 1)
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "Java", 2)
student_2.rate_lecture(lecturer_2, "Java", 1)
student_2.rate_lecture(lecturer_2, "Python", 1)
student_2.rate_lecture(lecturer_2, "C++", 10)
student_2.rate_lecture(lecturer_2, "Java", 2)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'C++', 10)
reviewer.rate_hw(student_2, 'Python', 10)
reviewer.rate_hw(student_2, 'Java', 10)



for student in all_students:
    print(student)
    print('\n')

print(f"Ольга лучше своего доппельгангера? {student > student_2}")
print('\n')
print('Лекторы:')
print(lecturer)
print('\n')
print(lecturer_2)
print('\n')
print(f"Новый преподаватель лучше старого? {lecturer < lecturer_2}")
print('\n')
print('Наблюдатели:')
print(reviewer)
print('\n')
print(reviewer_2)
print('\n')

python_grade = average_course_grade_student(all_students, 'Python')
print(f'Средняя оценка по курсу {python_grade[0]}, среди студентов равна - {python_grade[1]}')
C_grade = average_course_grade_student(all_students, 'C++')
print(f'Средняя оценка по курсу {C_grade[0]}, среди студентов равна - {C_grade[1]}')
Java_grade = average_course_grade_student(all_students, 'Java')
print(f'Средняя оценка по курсу {Java_grade[0]}, среди студентов равна - {Java_grade[1]}')

print('\n')

python_grade_lect = average_course_grade_lecturers(all_Lecturer, 'Python')
print(f'Средняя оценка по курсу {python_grade_lect[0]}, среди лекторов равна - {python_grade_lect[1]}')
C_grade_lect = average_course_grade_lecturers(all_Lecturer, 'C++')
print(f'Средняя оценка по курсу {C_grade_lect[0]}, среди лекторов равна - {C_grade_lect[1]}')
Java_grade_lect = average_course_grade_lecturers(all_Lecturer, 'Java')
print(f'Средняя оценка по курсу {Java_grade_lect[0]}, среди лекторов равна - {Java_grade_lect[1]}')