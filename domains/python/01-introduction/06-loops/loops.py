def non_negative_numbers_raised_twice(str_natural_number):
    output = []
    natural_number = int(str_natural_number)

    for index in range(natural_number):
        output.append(str(pow(index, 2)))

    return output


if __name__ == '__main__':
    print '\n'.join(non_negative_numbers_raised_twice(raw_input()))
