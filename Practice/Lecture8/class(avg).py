class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("Hello",self.name,"your avg marks is",sum/3)

s1 = student("Khadija",[99,90,78])
s1.avg()   
