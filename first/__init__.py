class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []

    def put_on(self, oll_courses):
        self.finished_courses.append(oll_courses)

    def grade_new(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_calculation(self):
        if not self.grades:
            return 0
        grades_list = []
        for new in self.grades.values():
            grades_list.extend(new)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f"""Имя: {self.name}
              \rФамилия: {self.surname}
              \rСредняя оценка за домашние задания: {self.average_calculation()}
              \rКурсы в процессе обучения: {', '.join(self.courses_in_progress)}
              \rЗавершенные курсы: {', '.join(self.finished_courses)}
        """

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise Exception('Ошибка!')
        return self.average_calculation() > other.average_calculation()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise Exception('Ошибка!')
        return self.average_calculation() < other.average_calculation()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('Ошибка!')
        return self.average_calculation() == other.average_calculation()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_calculation(self):
        if not self.grades:
            return 0
        grades_list = []
        for new in self.grades.values():
            grades_list.extend(new)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f"""Имя: {self.name}
              \rФамилия: {self.surname}
              \rСредняя оценка за лекции: {self.average_calculation()}
        """

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Ошибка!')
        return self.average_calculation() > other.average_calculation()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Ошибка!')
        return self.average_calculation() < other.average_calculation()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Ошибка!')
        return self.average_calculation() == other.average_calculation()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Сергей', 'Разумовский')
student_new = Student('Олег', 'Волков')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Java']
student_new.courses_in_progress += ['Python']
student_new.courses_in_progress += ['C++']
student_new.finished_courses += ['Java']

cool_reviewer = Reviewer('Игорь', 'Гром')
reviewer_new = Reviewer('Дмитрий', 'Дубин')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']
reviewer_new.courses_attached += ['Python']
reviewer_new.courses_attached += ['C++']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(student_new, 'Python', 9)
cool_reviewer.rate_hw(student_new, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'C++', 10)
cool_reviewer.rate_hw(best_student, 'C++', 8)
cool_reviewer.rate_hw(student_new, 'C++', 9)
cool_reviewer.rate_hw(student_new, 'C++', 8)
reviewer_new.rate_hw(best_student, 'Python', 9)
reviewer_new.rate_hw(best_student, 'Python', 10)
reviewer_new.rate_hw(student_new, 'Python', 4)
reviewer_new.rate_hw(student_new, 'Python', 7)
reviewer_new.rate_hw(best_student, 'C++', 9)
reviewer_new.rate_hw(best_student, 'C++', 8)
reviewer_new.rate_hw(student_new, 'C++', 3)
reviewer_new.rate_hw(student_new, 'C++', 8)

cool_lecturer = Lecturer('Евгений', 'Поэт')
lecturer_new = Lecturer('Кризалис', 'Силус')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']
lecturer_new.courses_attached += ['Python']
lecturer_new.courses_attached += ['C++']

best_student.grade_new(lecturer_new, 'Python', 9)
best_student.grade_new(lecturer_new, 'Python', 8)
best_student.grade_new(cool_lecturer, 'Python', 9)
best_student.grade_new(cool_lecturer, 'Python', 7)
best_student.grade_new(lecturer_new, 'C++', 9)
best_student.grade_new(lecturer_new, 'C++', 10)
best_student.grade_new(cool_lecturer, 'C++', 10)
best_student.grade_new(cool_lecturer, 'C++', 8)

student_new.grade_new(lecturer_new, 'Python', 9)
student_new.grade_new(lecturer_new, 'Python', 9)
student_new.grade_new(cool_lecturer, 'Python', 6)
student_new.grade_new(cool_lecturer, 'Python', 4)
student_new.grade_new(lecturer_new, 'C++', 9)
student_new.grade_new(lecturer_new, 'C++', 7)
student_new.grade_new(cool_lecturer, 'C++', 10)
student_new.grade_new(cool_lecturer, 'C++', 8)

print(best_student.grades)
print(student_new.grades)
print()
print(cool_lecturer.grades)
print(lecturer_new.grades)
print()
print(cool_reviewer)
print()
print(reviewer_new)
print()
print(cool_lecturer)
print()
print(lecturer_new)
print()
print(best_student)
print()
print(student_new)
print()

all_students = [best_student, student_new]
all_lecturers = [cool_lecturer, lecturer_new]
all_courses = input('Введите название курса: ')

print()

def compare_students(all_students, all_courses):
    grades_list = []
    for nil in all_students:
        grades_list.extend(nil.grades.get(all_courses, []))
    if not grades_list:
        return "По этому курсу оценки отсутствуют. "
    return round(sum(grades_list) / len(grades_list), 2)


def compare_lecturers(all_lecturers, all_courses):
    return compare_students(all_lecturers, all_courses)

print(f'Сравнение всех студентов по средним оценкам за домашние задания: '
          f'{best_student.name} {best_student.surname} {"получил результаты хуже, чем " if best_student < student_new else ("получил результаты лучше, чем " if best_student > student_new else "получил равные результаты с ")} {student_new.name} {student_new.surname}')
print()

print(f'Сравнение всех лекторов по средним оценкам за лекции: '
          f'{cool_lecturer.name} {cool_lecturer.surname} {"получил результаты хуже, чем" if cool_lecturer < lecturer_new else ("получил результаты лучше, чем" if cool_lecturer > lecturer_new else "получил равные результаты с ")} {lecturer_new.name} {lecturer_new.surname}')
print()

print(f"Средняя оценка для всех студентов по курсу {all_courses}: {compare_students(all_students, all_courses)}")
print()

print(f"Средняя оценка для всех лекторов по курсу {all_courses}: {compare_lecturers(all_lecturers, all_courses)}")
print()
