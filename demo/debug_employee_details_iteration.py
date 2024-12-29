from util import datautil


def main():
    print("Iterate through the list of employee objects ")
    employees = datautil.get_employee_data()
    for employee in employees:
        print("Employee name:{},salary:{},bonus:{} ".format(employee.name,employee.salary,employee.get_bonus()))

    print("Completed iteration")


if __name__ == '__main__':
    main()
