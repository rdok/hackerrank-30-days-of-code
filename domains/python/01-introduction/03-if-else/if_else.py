def isEven( number ):
    return number % 2 == 0

def isOdd( number ):
    return not isEven( number )

def isWeird( number ):
    number = int( number )

    return isOdd( number ) or ( isEven( number ) and 6 <= number <= 20 )

if __name__ == '__main__':

    output = 'Not Weird'

    if isWeird(raw_input()):
        output = 'Weird'

    print output
