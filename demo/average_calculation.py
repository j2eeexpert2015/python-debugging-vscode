def calculate_average(input):
    result = 0
    for element in input:
        result = result + element

    result = result / len(input)
    return result;


def main():
    print("Average Calculation")
    numbers = [10, 20, 30]
    average = calculate_average(numbers)
    print("Average is {}".format(average))


if __name__ == '__main__':
    main()
