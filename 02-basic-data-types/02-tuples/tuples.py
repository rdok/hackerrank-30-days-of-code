if __name__ == '__main__':
    length = raw_input()
    tupleValues = tuple(map(int, raw_input().split(' ')))

    print hash(tupleValues)
