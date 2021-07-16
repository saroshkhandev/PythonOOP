class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward
    def annual_salary(self):
        return (self.pay * 12) + self.reward

class Employee:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal

    def final_salary_m(self):
        return self.final_salary.annual_salary()
    
    def display(self):
        print("Your Name: ", self.name)
        print("Position: ", self.position)

sal = Salary(120000, 20000)

emp = Employee("Sarosh", "Backend Dev", sal)
emp.display()
print(emp.final_salary_m())
