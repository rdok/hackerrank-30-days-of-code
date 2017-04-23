from __future__ import division

def handleDivisionTypes(firstNumber, secondNumber):

    firstNumber = int( firstNumber )

    secondNumber = int( secondNumber )

    integerDivision = str( firstNumber // secondNumber );

    floatDivision = str ( firstNumber / secondNumber );

    return [ integerDivision, floatDivision ];


if __name__ == '__main__':

    firstNumber = raw_input()

    secondNumber = raw_input()

    print '\n'.join(handleDivisionTypes(firstNumber, secondNumber))
