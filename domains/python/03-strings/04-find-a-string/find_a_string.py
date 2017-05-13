import sys

if __name__ == '__main__':
    string = raw_input()
    substring = raw_input()
    substringLength = len( substring )
    count = 0

    for index in range(len(string)):
        if( string[ index : index + substringLength ] == substring ):
            count =  count + 1

    print count
