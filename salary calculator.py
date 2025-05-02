class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def give_bonus(self):
        bonus = self.salary*0.10
        self.salary += bonus
        return self.salary
