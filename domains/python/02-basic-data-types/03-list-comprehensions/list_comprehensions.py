import sys

if __name__ == '__main__':
    xCoordinate = int( raw_input() )
    yCoordinate = int( raw_input() )
    zCoordinate = int( raw_input() )
    unacceptableSum = int( raw_input() )

    comprenhensiveList = [
        [xValue, yValue, zValue] 
        for xValue in range(xCoordinate + 1) 
        for yValue in range(yCoordinate + 1)
        for zValue in range(zCoordinate + 1)
        if( ( xValue + yValue + zValue ) != unacceptableSum)
    ]

    print comprenhensiveList
