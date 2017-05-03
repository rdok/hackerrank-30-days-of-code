import sys

if __name__ == '__main__':
    totalNumbers = int( raw_input() )
    numbers = map(int, raw_input().split())
    print numbers

    largestNumber = numbers.pop()
    secondLargestNumber = largestNumber

    for number in numbers:
        if( largestNumber >= number ):
            continue

        secondLargestNumber = largestNumber
        largestNumber = number

    print secondLargestNumber
