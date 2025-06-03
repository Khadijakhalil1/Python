class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f" The square of {self.n}  is  ={self.n*self.n}")
    def squareRoot(self):
        print(f"The squareRoot of{self.n} is ={self.n**1/2}")
    def Cube(self):
        print(f"  The cube of  {self.n}  is  ={self.n*self.n*self.n}")

k=calculator(4)
k.square()
k.squareRoot()
k.Cube()
                