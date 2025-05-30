class programmer:
    company = "Google"
    def __init__(self,name,salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Khadija",207230,3344)
print(p.name,p.salary,p.pin,p.company)