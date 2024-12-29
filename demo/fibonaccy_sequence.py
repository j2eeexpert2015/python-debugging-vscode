# Fibonacci Sequence , expected output :1,1,2,3,5,8,13,....

def main():
    fib = get_fibonacci(8)
    print("Fibonacci is :{}".format(fib))


def get_fibonacci(input):
    # check for the terminating condition
    if input <= 1:
        # Return the value for position 1, here it is 0
        return 0
    if input == 2:
        # return the value for position 2, here it is 1
        return 1

    n_1 = get_fibonacci(input - 1)

    n_2 = get_fibonacci(input - 2)

    n = n_1 + n_2
    # return the fibo number
    return n


if __name__ == '__main__':
    main()
