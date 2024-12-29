from util import datautil
from model.Person import Person


def main():
    sample_number = 100
    sample_string ="Dummy String"
    sample_array = ['A', 'B', 'C', 'D', 'E']
    person_list = datautil.get_person_list_with_other_data_types()
    sample_dict = {"key_string": "James", "key_integer": 25}
    sample_set = {1, 2, 3}
    print("Program completed ...")


if __name__ == '__main__':
    main()