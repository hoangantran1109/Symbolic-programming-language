"""
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...). (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 point)

c) Draw a UML class diagram for your Employee class. (1 point)
"""

import re

class Employee:
    #CONSTRUCTOR DER KLASSE EMPLOYEE
    def __init__(self, id,department, name):

        self.id = id
        self.department = department
        self.name = name

    """ * dies Set-Method beschreibt das Nennen eines Names. 
    """
    def set_name(self, name):
        if (not type(name) == str):
            raise TypeError
        if not re.match("\W+( \W+)*", name.strip()):
            raise ValueError
        self.name = name

    """ * dies Set-Method beschreibt das Einstelln eines ID von Employee. 
    """
    def set_id(self, id):
        if(not type(id) == int):
            raise TypeError
        self.id = id

    """ * dies Set-Method beschreibt das Einstelln eines Department von Employee. 
    """
    def set_department(self, department):
        if (not type(department) == str):
         raise TypeError
        if not re.match(r"\w( \w+)*", department.strip()):
         raise ValueError
        self.department = department

    def __str__(self):
        res = "*** Employer Info ***\n"
        res += "Employer Name:" + self.name + "\n"
        res += "Employer ID:" + str(self.id) + "\n"
        res += "Department:" + self.department + "\n"
        return res

if __name__ == "__main__":
    print("Employee application")
    emp1 = Employee(id, 'department','name')
    emp2 = Employee(39118, 'IT','Nguyen Thao Anh Phan')
    print(emp2)
    emp1.set_id(47899)
    emp1.set_department('IT')
    emp1.set_name('Hoang An Tran')
    print(emp1)




