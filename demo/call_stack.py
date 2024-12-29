dummy_global_var = 0
def method3(input):
    dummy_var_3 = 3
    dummy_global_var=3
    return input + 1


def method2(input):
    dummy_var_2 = 2
    dummy_global_var=2
    return method3(input) * 10


def method1(input):
    dummy_var_1 = 1
    dummy_global_var=1
    return method2(input) * 200


def main():
    result = method1(100)


if __name__ == '__main__':
    main()
