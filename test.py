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

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = Student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
