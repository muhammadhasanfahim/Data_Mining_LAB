# Question_01
class Student:
    pass
class Marks:
    pass

fahim_064 = Student()
passed = Marks()
student = isinstance(fahim_064, Student)
print("fahim_064 is a instance of class Student--", student)
marks = isinstance(fahim_064, Marks)
print("fahim_064 is a instance of class Marks--", marks)
student = isinstance(passed, Student)
print("passed is a instance of class Student--", student)
marks = isinstance(passed, Marks)
print("passed is a instance of class Marks--", marks)
student_subclass = isinstance(Student, object)
print("Student class is a subclass of object--", student_subclass)
marks_subclass = isinstance(Marks, object)
print("Marks class is a subclass of object--", marks_subclass)

# Question_02
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

e1 = Student("Fahim", 64)
print(e1.name, e1.marks)
e1.name = "Ahmed"
e1.marks = 73
print("modified value:", e1.name, e1.marks)

# Question_03
class Student:
    def __init__(self, StudentID, StudentName):
        self.ID = StudentID
        self.Name = StudentName
    
e1 = Student("201902064", "Fahim")
print(e1.ID, e1.Name)
# adding new attribute to this class
e1.Marks = 82
print("New attribute=> Marks: ",e1.Marks)
# deleting attribute
del e1.Marks
print("Deleted attribute=> Marks: ",e1.Marks)

# Question_04
class Student:
    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName
    def function(self):
        print(f"Student name is {self.StudentName} & ID is {self.StudentID}")

e1 = Student("201902064", "Fahim")
e1.function()