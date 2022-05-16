class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress or course in self.finished_courses \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Лектор не преподает данный курс'

    def percent(self):
        all_grade = []
        for first_grade in self.grades.values():
            for grade in first_grade:
                all_grade.append(grade)
        percent = sum(all_grade) / len(all_grade)
        return percent

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.percent()} \n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)} \n'
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.percent() > other.percent():
                print(
                    f'Студент {self.name} {self.surname} лучше выполняет домашние работы, чем студент {other.name} {other.surname}.\n')
            elif self.percent() < other.percent():
                print(
                    f'Студент {other.name} {other.surname} лучше выполняет домашние работы, чем студент {self.name} {self.surname}.\n')
            else:
                print(
                    f'У студентов {other.name} {other.surname} и {self.name} {self.surname} одинаковые показатели по домашнему заданию.\n')
        else:
            print('Ошибка сравнения')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Student.percent(self)} \n'
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if Student.percent(self) > Student.percent(other):
                print(f'Преподователь {self.name} {self.surname} лучше преподователя {other.name} {other.surname}\n')
            elif Student.percent(self) < Student.percent(other):
                print(f'Преподователь {other.name} {other.surname} лучше преподавателя {self.name} {self.surname}\n')
            else:
                print(
                    f'У преподователя {other.name} {other.surname} и {self.name} {self.surname} одинаковые рейтинги\n')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Студент не учится на данном курсе'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


student_1 = Student('Ryiot', 'Emaly', 'woman')
student_1.courses_in_progress += ['Python', 'Design', '1C', 'C++']
student_1.finished_courses += ['Manager']

student_2 = Student('Sam', 'Ralf', 'man')
student_2.courses_in_progress += ['Java', 'Manager', '1C', 'C++']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Jack', 'Tyson')
lecturer_1.courses_attached += ['Java', 'Python', '1C']

lecturer_2 = Lecturer('Amanda', 'Waller')
lecturer_2.courses_attached += ['Manager, Design', 'C++']

reviewer_1 = Reviewer('Tim', 'Cick')
reviewer_1.courses_attached += ['Python', 'Java', '1C']
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Java', 2)
reviewer_1.rate_hw(student_2, 'Java', 8)
reviewer_1.rate_hw(student_1, '1C', 5)
reviewer_1.rate_hw(student_1, '1C', 9)
reviewer_1.rate_hw(student_2, '1C', 10)
reviewer_1.rate_hw(student_2, '1C', 2)

reviewer_2 = Reviewer('Ban', 'Parker')
reviewer_2.courses_attached += ['Manager', 'Design', 'C++']
reviewer_2.rate_hw(student_2, 'Manager', 7)
reviewer_2.rate_hw(student_2, 'Manager', 10)
reviewer_2.rate_hw(student_1, 'Design', 5)
reviewer_2.rate_hw(student_1, 'Design', 3)
reviewer_2.rate_hw(student_1, 'C++', 6)
reviewer_2.rate_hw(student_1, 'C++', 8)
reviewer_2.rate_hw(student_2, 'C++', 7)
reviewer_2.rate_hw(student_2, 'C++', 6)

student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Design', 6)
student_1.rate_lecturer(lecturer_2, 'Design', 8)
student_1.rate_lecturer(lecturer_2, 'C++', 6)
student_1.rate_lecturer(lecturer_2, 'C++', 8)
student_1.rate_lecturer(lecturer_1, '1C', 7)
student_1.rate_lecturer(lecturer_1, '1C', 1)

student_2.rate_lecturer(lecturer_1, 'Java', 2)
student_2.rate_lecturer(lecturer_1, 'Java', 8)
student_2.rate_lecturer(lecturer_2, 'Manager', 5)
student_2.rate_lecturer(lecturer_2, 'Manager', 10)
student_2.rate_lecturer(lecturer_2, 'C++', 7)
student_2.rate_lecturer(lecturer_2, 'C++', 9)
student_2.rate_lecturer(lecturer_1, '1C', 5)
student_2.rate_lecturer(lecturer_1, '1C', 2)
print(student_1)
print(lecturer_1)
print(reviewer_1)

student_1.__lt__(student_2)
lecturer_1.__lt__(lecturer_2)

student_list = [student_1, student_2]


def stud_percent(course):
    stud_grades = []
    for student in student_list:
        for grades in student.grades.items():
            if course in grades[0]:
                stud_grades += grades[1]
    return print(f'Средняя оценка у студентов по курсу {course} = {sum(stud_grades) / len(stud_grades)}.')




stud_percent('C++')

lecturer_list = [lecturer_1, lecturer_2]


def lecturer_percent(course):
    lect_grades = []
    for lecturer in lecturer_list:
        for grades in lecturer.grades.items():
            if course in grades[0]:
                lect_grades += grades[1]
    print(f'Средняя оценка у лекторов по курсу {course} = {sum(lect_grades) / len(lect_grades)}.')


lecturer_percent('Design')