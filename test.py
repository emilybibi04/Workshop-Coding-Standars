"""
Module test.py
This script contains the definition and logic for managing students.
"""
class Student:
    """
    Class representing a Student object
    """
    def __init__(s, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def addGrades(self, g):
        self.gradez.append(g)

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        return t / len(self.gradez)

    def check_honor(self):
        """ Checks if the student is an honor student based on their average grade """
        if self.calcAverage() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """Deletes a grade at the specified index from the student's grade list"""
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.calcaverage())


def startrun():
    """
    Program entry point
    """
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
