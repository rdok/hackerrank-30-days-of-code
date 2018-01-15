def arithmetic_operator_analysis(first_number, second_number):
    first_number = int(first_number)

    second_number = int(second_number)

    num_sum = str(first_number + second_number)

    difference = str(first_number - second_number)

    product = str(first_number * second_number)

    return [num_sum, difference, product]


if __name__ == '__main__':
    first_input = raw_input()

    second_input = raw_input()

    print '\n'.join(arithmetic_operator_analysis(first_input, second_input))
