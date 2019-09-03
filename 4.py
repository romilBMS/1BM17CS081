class Student:
    def __init__(self):
        self.id=self.age=self.marks=None
    def setValues(self, id,age,marks):
        self.id=id
        self.age=age
        self.marks=marks
    
    def getValues(self):
        print("ID:",self.id,"\nage:",self.age,"\nmarks:",self.marks)
    
    def validate_age(self,age):
        return self.age>=20
    def validate_marks(self,marks):
        return self.marks>=0 and self.marks<=100
    def check_qualification(self):
        return self.validate_age(self.age) and self.validate_marks(self.marks) and self.marks>=65
    
s1=Student()
s2=Student()

s1.setValues(25,22,66)
s2.setValues(34,66,99)

if s1.check_qualification():
    s1.getValues()
if s2.check_qualification():
    s2.getValues()


    
    