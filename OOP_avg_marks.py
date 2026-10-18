class Student:
    def __init__(self,name,marks): # self = Object
        self.name = name
        self.marks = marks
    def getavg(self):    
        self.avg = (self.marks[0]+self.marks[1]+self.marks[2])/3
        print(f"The average marks of {self.name} is {self.avg}")

s1 = Student("Hashir",[5,7,3])
s1.getavg()
s1.name = "Ir"
s1.getavg()