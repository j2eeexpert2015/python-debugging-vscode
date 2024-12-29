from model.Person import Person
from model.Employee import Employee


def get_person_list_with_other_data_types():
    persons = []
    p1 = Person("Steve", 40, "US")
    p2 = Person("Martin", 50, "Germany")
    p3 = Person("Philip", 20, "Netherlands")
    p4 = Person("Marco", 20, "Netherlands")
    p5 = Person("Ricky", 30, "UK")
    p6 = Person("Peter", 40, "Denmark")
    p7 = Person("Mark", 55, "Norway")
    p8 = Person("Ian", 30, "Finland")
    p9 = Person("Brian", 60, "Netherlands")

    persons.append(p1)
    persons.append(p2)
    persons.append(p3)
    persons.append(p4)
    persons.append(p5)
    persons.append(p6)
    persons.append(p7)
    persons.append(p8)
    persons.append(p9)
    persons.append("Dummy Data")
    return persons


def get_employee_data():
    employees = []
    e1 = Employee("Steve", 40, 1000)
    e2 = Employee("Ricky", 25, 1000)
    e3 = Employee("Ian", 56, 3000)
    e4 = Employee("Mathew", 50, 5000)
    e5 = Employee("Glenn", 30, 6000)
    e6 = Employee("Stephen", 40, 1000)
    e7 = Employee("Michael", 25, 1000)
    e8 = Employee("Patt", 56, 3000)
    e9 = Employee("David", 0, 5000)
    e10 = Employee("Mike", 30, 6000)

    employees.append(e1)
    employees.append(e2)
    employees.append(e3)
    employees.append(e4)
    employees.append(e5)
    employees.append(e6)
    employees.append(e7)
    employees.append(e8)
    employees.append(e9)
    employees.append(e10)

    return employees
