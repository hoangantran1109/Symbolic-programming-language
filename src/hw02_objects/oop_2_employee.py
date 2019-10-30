"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...). (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 point)

c) Draw a UML class diagram for your Employee class. (1 point)
"""


class Employee:
    def __init__(self, num, id,department, name):
        self.emp_num = num
        self.emp_id = id
        self.emp_department = department
        self.emp_name = name

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_department(self, department):
        self.department = department

    def __str__(self):
        res = "*** Employer Info ***\n"
        res += "Employer Name:" + self.name + "\n"
        res += "Employer ID:" + str(self.id) + "\n"
        res += "Department:" + self.emp_department + "\n"
        return res

if __name__ == "__main__":
    print("Employee application")
    emp1 = Employee('name', 'id', 'department', 'title')
    emp2 = Employee('name', 'id', 'department', 'title')
    emp1.set_name('Susan Meyers')
    emp1.set_id('47899')
    emp1.set_department('Accounting')
    emp1.set_title('Vice President')

    emp2.set_name('Mark Jones')
    emp2.set_id('39119')
    emp2.set_department('IT')
    emp2.set_title('Programmer')
