def arithmetic_operator_analysis(first_input, second_input):
    first_number = int(first_input)

    second_number = int(second_input)

    num_sum = str(first_number + second_number)

    difference = str(first_number - second_number)

    product = str(first_number * second_number)

    return [num_sum, difference, product]


if __name__ == '__main__':
    first_number = raw_input()

    second_number = raw_input()

    print '\n'.join(arithmetic_operator_analysis(first_number, second_number))
