if __name__ == '__main__':
    length = raw_input()
    elements = raw_input().split(' ')
    sequence = map(int, elements)
    tupleValues = tuple(sequence)

    print hash(tupleValues)
