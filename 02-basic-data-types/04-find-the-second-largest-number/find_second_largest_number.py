def remove_all(value, listValue):
    return filter(lambda number: number != value, listValue)


if __name__ == '__main__':
    totalNumbers = int(raw_input())
    numbers = map(int, raw_input().split())

    largestNumber = max(numbers)

    numbers = remove_all(largestNumber, numbers)

    secondLargestNumber = max(numbers)

    print secondLargestNumber
