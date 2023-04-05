class Student:
    #st_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        #Student.st_list.append(self)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        grades_list = list(self.grades.values())
        total_list = []
        for course in grades_list:
            for grade in course:
                total_list.append(grade)
            avg_grade = sum(total_list)/len(total_list)
        self.avg_grade = avg_grade
        return avg_grade

    def __lt__(self, other):
        if self.avg_grade > other.avg_grade:
            print(f'Средняя оценка за дз выше у {self.name}')
        elif self.avg_grade < other.avg_grade:
            print(f'Средняя оценка за дз выше у {other.name}')
        else:
            print(f'Средние оценки за дз у {self.name} и {other.name} равны')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        grades_list = list(self.grades.values())
        for course in grades_list:
            avg_grade = sum(course)/len(course)
            self.avg_grade = avg_grade
        return avg_grade

    def __lt__(self, other):
        if self.avg_grade > other.avg_grade:
            print(f'Средняя оценка за лекции у {self.name} выше, чем у {other.name}')
        elif self.avg_grade < other.avg_grade:
            print(f'Средняя оценка за лекции у {other.name} выше, чем у {self.name}')
        else:
            print(f'Средние оценки за лекции у {self.name} и {other.name} равны')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}'
        return res

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

students_list = []
peregrin = Student('Peregrin', 'Took', 'hobbit')
meriadoc = Student('Meriadoc', 'Brandybuck','hobbit')
students_list.append(peregrin)
students_list.append(meriadoc)

lecturers_list = []
gandalf = Lecturer('Gandalf', 'The Grey')
legolas = Lecturer('Legolas', 'of Mirkwood')
lecturers_list.append(gandalf)
lecturers_list.append(legolas)

galadriel = Reviewer('Galadriel','of Lothlorien')
elrond = Reviewer('Elrond','of Rivendell')

galadriel.courses_attached += ['Horse-riding', 'Archery', 'Using Palantir']
elrond.courses_attached += ['Horse-riding', 'Archery']
gandalf.courses_attached += ['Horse-riding', 'Using Palantir']
legolas.courses_attached += ['Archery', 'Horse-riding']

peregrin.courses_in_progress += ['Horse-riding', 'Archery', 'Using Palantir']
meriadoc.courses_in_progress += ['Horse-riding', 'Archery', 'Using Palantir']
peregrin.finished_courses += ['Growth']
meriadoc.finished_courses += ['Growth']

galadriel.rate_hw(peregrin,'Horse-riding', 8)
galadriel.rate_hw(meriadoc,'Horse-riding', 9)
galadriel.rate_hw(peregrin,'Archery', 9)
galadriel.rate_hw(meriadoc, 'Archery', 8)

elrond.rate_hw(peregrin,'Horse-riding', 8)
elrond.rate_hw(meriadoc,'Horse-riding', 9)
elrond.rate_hw(peregrin,'Archery', 9)
elrond.rate_hw(meriadoc, 'Archery', 8)

peregrin.rate_lec(gandalf, 'Horse-riding', 10)
meriadoc.rate_lec(gandalf, 'Horse-riding', 10)
peregrin.rate_lec(legolas, 'Horse-riding', 9)
meriadoc.rate_lec(legolas, 'Horse-riding', 10)
peregrin.rate_lec(legolas, 'Archery', 9)
meriadoc.rate_lec(legolas, 'Archery', 10)

grades_list = []
course_grades = []
def course_avg_grade(students, course):
  for student in students:
    grades_list.append(student.grades[course])
  for student, el in grades_list:
    course_grades.append(el)
  avg_grade = sum(course_grades)/len(course_grades)
  return avg_grade


print(f'Reviewers:\n{galadriel}\n{elrond}\n')
print(f'Lecturers:\n{gandalf}\n{legolas}\n')
print(f'Students:\n{peregrin}\n{meriadoc}\n')

print(gandalf.__lt__(legolas))
print(peregrin.__lt__(meriadoc))

print(f'Средняя оценка студентов за домашние задания по курсу Archery: {course_avg_grade(students_list, "Archery")}')
print(f'Средняя оценка лекторов за домашние задания по курсу Horse-riding: {course_avg_grade(lecturers_list, "Horse-riding")}')