class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_bonus(self):
        bonus = (self.salary / self.age) * 1000
        return bonus
