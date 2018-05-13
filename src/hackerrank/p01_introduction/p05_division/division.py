from __future__ import division


def handle_division_types(first_input, second_input):
    first_number = int(first_input)

    second_number = int(second_input)

    integer_division = str(first_number // second_number)

    float_division = str(first_number / second_number)

    return [integer_division, float_division]


if __name__ == '__main__':
    firstNumber = raw_input()

    secondNumber = raw_input()

    print '\n'.join(handle_division_types(firstNumber, secondNumber))
