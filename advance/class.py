class Employee:
    id = 10
    name = 'asif'
    def display (self):
        print('id = %s and Name = %s' % (self.id, self.name))
if __name__ == '__main__':
    emp = Employee()
    emp.display()