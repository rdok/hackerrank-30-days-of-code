def arithmeticOperatorAnalysis(firstNumber, secondNumber):

    firstNumber = int( firstNumber )

    secondNumber = int( secondNumber )

    numSum = str( firstNumber + secondNumber );

    difference = str( firstNumber - secondNumber );

    product = str( firstNumber * secondNumber );

    return [ numSum, difference, product ];


if __name__ == '__main__':

    firstNumber = raw_input()

    secondNumber = raw_input()

    print '\n'.join(arithmeticOperatorAnalysis(firstNumber, secondNumber))
