import sys
def removeAll(value, listValue):
    return filter( lambda number: number != value, listValue)


if __name__ == '__main__':
    totalNumbers = int( raw_input() )
    numbers = map(int, raw_input().split())

    largestNumber = max(numbers)

    numbers = removeAll(largestNumber, numbers)

    secondLargestNumber = max(numbers)

    print secondLargestNumber
