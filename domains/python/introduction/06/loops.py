def nonNegativeNumbersRaisedTwice(strNaturalNumber):
    output = [];
    naturalNumber = int(strNaturalNumber)

    for index in range(naturalNumber):
        output.append(str(pow(index, 2)))

    return output

if __name__ == '__main__':
    print '\n'.join(nonNegativeNumbersRaisedTwice(raw_input()))
