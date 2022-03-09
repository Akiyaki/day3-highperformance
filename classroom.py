#import numpy as np

class Person:
        def __init__(self, firstname, lastname):
                self.firstname = firstname
                self.lastname = lastname

        def fullname(self):
                return self.firstname + " " + self.lastname

#Dabicha = Person("David", "Sandberg")
#print(Dabicha.fullname())


class Student(Person):
        def __init__(self, firstname, lastname, physics, math):
                super().__init__(firstname, lastname)
                self.physics = physics
                self.math = math

        def scores(self):
                return ": Physics - " + str(self.physics) + " " + "Mathematics - " + str(self.math)

        def results(self):
#                print(self.fullname() + self.scores()) 
                return self.fullname() + self.scores()


#Dabicha = Student("David", "Sandberg", 30, 50)
#print(Dabicha.fullname() + Dabicha.scores())             
            
class Teacher(Person):
        def __init__(self, firstname, lastname, course):
                super().__init__(firstname, lastname)
                self.course = course

        def courseinfo(self):
                return " "  + self.course

#Dabicha = Teacher("David", "Sandberg", "Physics")
#print(Dabicha.fullname() + Dabicha.courseinfo())
