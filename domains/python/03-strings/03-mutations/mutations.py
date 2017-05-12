import sys

if __name__ == '__main__':
    string = list( raw_input() )
    secondLine = raw_input().split()
    index = int( secondLine[0] )
    character = secondLine[1]

    string[ index ] = character
    string = ''.join(string)

    print string
