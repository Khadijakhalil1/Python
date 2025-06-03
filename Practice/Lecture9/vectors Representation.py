class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
       
    def show(self):
        print(f"print the 2D Vector {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super(). __init__(i,j)
        self.k=k
    
    def show(self):
        print(f"print the 3D Vector {self.i}i + {self.j}j + {self.k}k")
        
o=TwoDVector(3,7)
o.show()
p=ThreeDVector(2,4,6)
p.show()       