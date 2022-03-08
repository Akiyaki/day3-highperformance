#import numpy as np

class Person:
        def __init__(self, firstname, lastname):
                self.firstname = firstname
                self.lastname = lastname

        def fullname(self):
                return self.firstname + " " + self.lastname


Dabicha = Person("David", "Sandberg")
print(Dabicha.fullname())

