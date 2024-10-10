#Python Object Oriented Programming

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return(f"{self.first} {self.last}")
    
    def firstnameAndSalary(self):
        return(f"{self.first} {self.pay}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return(self.pay)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
    
    def __add__(self):
        return f"{self.pay}"

    def __repr__(self):
        return Employee(f"{self.first} {self.last} {self.pay}")

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang




class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def all_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())     




dev_1 = Employee("Dennis","Amematekpor", 602340)
mgr_1 = Manager("Tracy","Lover", 77788, [dev_1])
emp2 = Developer("Tracy","Ghana", 77788,"Python")


emp_str_1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2000, 1, 22)

mgr_1.add_emp(emp2)

#print(mgr_1.email)
#mgr_1.all_emps()
#print(mgr_1.employees[0].fullname())

mgr_1.remove_emp(dev_1)
#mgr_1.all_emps()

#print(isinstance(mgr_1, Employee))
#print(issubclass(Manager, Developer))

print(dev_1)
print(str(dev_1))
print(dev_1 + mgr_1)
print(len(emp2))