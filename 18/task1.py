class Student:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year
        self.__grades = []
    def add_grade(self, grade):
        try:
            grade = int(grade)
        except ValueError:
            print(f'{grade} не является целым числом')
            return None
        self.__grades.append(grade)
    def get_average_grade(self):
        if len(self.__grades) != 0:
            return sum(self.__grades)/len(self.__grades)
        else:
            return None
    def promote(self):
        if self.__year < 5:
            self.__year += 1
    def __str__(self):
        return f'Студент {self.__name}, {self.__year} курс, средний балл {self.get_average_grade()}'
    def get_name(self):
        return self.__name

class Proffesor:
    def __init__(self, name):
        self.__name = name
        self.__students = []
    def add_students(self, student):
        if isinstance(student, Student):
            self.__students.append(student)
    def remove_student(self, name):
        for i, student in enumerate(self.__students):
            if student.get_name() == name:
                return self.__students.pop(i)
    def get_all_averages(self):
        for student in self.__students:
            print(student)
    def find_top_student(self):
        return max(self.__students, key = lambda x: x.get_average_grade())
        
s = Student('Иван',3)
s2 = Student('Илья',3)
s3 = Student('Сергей',3)
s.add_grade(5)
s.add_grade(5)
s.add_grade(5)
s.add_grade(4)
s2.add_grade(4)
s2.add_grade(4)
s2.add_grade(4)
s2.add_grade(4)
s2.add_grade(4)
s3.add_grade(3)
s3.add_grade(3)
s3.add_grade(3)
s3.add_grade(3)
s3.add_grade(3)
s3.add_grade(3)
s3.add_grade(2)
s3.add_grade(4)
s3.add_grade(4)

prof = Proffesor('Олег Евгеньевич')
prof.add_students(s)
prof.add_students(s2)
prof.add_students(s3)
