import sys

if __name__ == '__main__':
    xCoordinate = int( raw_input() )
    yCoordinate = int( raw_input() )
    zCoordinate = int( raw_input() )
    unacceptableSum = int( raw_input() )
    comprenhensiveList = []

    for xValue in range(xCoordinate):
        for yValue in range(yCoordinate):
            for zValue in range(zCoordinate):
                if( ( xValue + yValue + zValue ) != unacceptableSum):
                    comprenhensiveList.append( [xValue, yValue, zValue] )

    print comprenhensiveList
