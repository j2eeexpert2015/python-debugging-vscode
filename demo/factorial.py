def get_factorial(n):
    result = 1
    if n > 1:
        result = n * get_factorial(n - 1)
    return result


def main():
    input = 5
    factorial = get_factorial(input)
    print("Factorial of {} is :{}".format(input, factorial))


if __name__ == '__main__':
    main()
