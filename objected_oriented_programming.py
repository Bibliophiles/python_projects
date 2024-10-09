#Python Object Oriented Programming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"

    def fullname(self):
        return(f"{self.first} {self.last}")
    
    def firstnameAndSalary(self):
        return(f"{self.first} {self.pay}")


emp1 = Employee("Dennis","Amematekpor", 602340)
emp2 = Employee("Tracy","Ghana", 77788)

print(emp1.fullname())
print(emp2.fullname())
print(emp2.firstnameAndSalary())
print(emp2.email)