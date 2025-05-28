class emp:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print("Role =",self.role)
        print("Department =",self.dept)
        print("salary =",self.sal)
class engineer(emp):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")
    
engg1  =engineer("Khalil",51)
engg1.showDetails()

