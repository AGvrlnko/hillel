class StudentsError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age: {self.age}, gender: {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age: {self.age}, gender: {self.gender}, record book: {self.record_book}'


class Group:

    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise StudentsError('У групі не може бути більше 10 студентів')

        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)

        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = ''

        for student in self.group:
            all_students += str(student) + '\n'

        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')

students = [
    Student('Male', 30, 'Steve', 'Jobs', 'AN142'),
    Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
    Student('Male', 20, 'John', 'Smith', 'AN146'),
    Student('Female', 21, 'Anna', 'Brown', 'AN147'),
    Student('Male', 22, 'Tom', 'Hardy', 'AN148'),
    Student('Female', 23, 'Kate', 'Wilson', 'AN149'),
    Student('Male', 24, 'Bob', 'Dylan', 'AN150'),
    Student('Female', 25, 'Mary', 'Stone', 'AN151'),
    Student('Male', 26, 'Jack', 'Black', 'AN152'),
    Student('Female', 27, 'Sara', 'Connor', 'AN153'),
    Student('Male', 28, 'Peter', 'Parker', 'AN154')
]

try:
    for student in students:
        gr.add_student(student)

except StudentsError as error:
    print(error)

print(gr)