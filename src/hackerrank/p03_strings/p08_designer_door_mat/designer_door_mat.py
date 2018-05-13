def process():
    rows, columns = map(int, raw_input().split())
    for upperIndex in xrange(1, rows, 2):
        print (columns - (upperIndex * 3)) / 2 * '-' + upperIndex * '.|.' + (columns - (upperIndex * 3)) / 2 * '-'
    print (columns / 2 - (len('WELCOME') / 2)) * '-' + 'WELCOME' + (columns / 2 - (len('WELCOME') / 2)) * '-'
    for lowerIndex in xrange(rows - 2, -1, -2):
        print (columns - (lowerIndex * 3)) / 2 * '-' + lowerIndex * '.|.' + (columns - (lowerIndex * 3)) / 2 * '-'


if __name__ == "__main__":
    process()
