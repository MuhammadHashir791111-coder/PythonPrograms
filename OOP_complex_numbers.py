class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    @property
    def show(self):
        return f"{self.real}i + {self.imaginary}j"
    def __add__(num1, num2):  #num1 = self
        newreal = num1.real + num2.real
        newimaginary = num1.imaginary + num2.imaginary
        return Complex(newreal,newimaginary)
    def __sub__(num1, num2): #num1 = self               most programmers write it like: 
        newreal = num1.real - num2.real       #                              def __sub__(self, num2):
        newimaginary = num1.imaginary - num2.imaginary
        return Complex(newreal,newimaginary)
        

num1 = Complex(3,4)        
print(num1.show)

num2 = Complex(1,2)
print(num2.show)

num3 = num1 + num2
print(num3.show)

num4 = num3 - num2
print(num4.show)
