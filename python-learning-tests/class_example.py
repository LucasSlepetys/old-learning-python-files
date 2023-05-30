
#! Python Object-Oriented Programming Examples

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ('{}.{}@company.com').format(first.lower(),last.lower())

        Employee.num_of_emps += 1

    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        #* 5, 6 = saturday & sunday
        if day.weekday() == 5 or day.weekday() == 6: 
            return False
        return True   



#! Create instaces:
emp_1 = Employee('Lucas', 'Slepetys', 5000)
emp_2 = Employee('Test', 'User', 6000)


import datetime
my_date = datetime.date(2021, 10, 2)

print(Employee.is_workday(my_date))






#! a class from a string
emp_str_1 = 'John-Doe-70000'

#* Create a instace by using a string with its values
emp_3 = Employee.from_string(emp_str_1)

Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(emp_3.__dict__)

#todo -> (Python OOP Tutorial 4: Inheritance - Creating Subclasses)


