class emp:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print("Role =",self.role)
        print("Department =",self.dept)
        print("salary =",self.sal)

e1 = emp("Accountant","Finance","70,000")
e1.showDetails()