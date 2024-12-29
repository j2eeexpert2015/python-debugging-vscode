from util import datautil
from model.Person import Person


def main():
    print("Iterate through the list of person objects ")
    persons = datautil.get_person_list_with_other_data_types()
    for person in persons:
        print("Person name:{},age:{},country:{} ".format(person.name, person.age, person.country))

    print("Completed iteration".format(person))


if __name__ == '__main__':
    main()
