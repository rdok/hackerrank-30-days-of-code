if __name__ == '__main__':
    height = int(raw_input())
    width = int(raw_input())

    filler = '-'
    pattern = '.|.'

    leftPart = filler * (width / 2 - 1)
    middle = pattern
    rightPart = filler * (width / 2 - 1)

    print leftPart + middle + rightPart
