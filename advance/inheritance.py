class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name = %s and Age = %d' % (self.name, self.age) )


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def displayStudent(self):
        print('name = %s, Age = %d and Course = %s' % (self.name, self.age, self.course) )


if __name__ == '__main__':
    asif = Student('ASIF', 22, 'MCA')
    asif.displayStudent()