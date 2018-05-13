def dividable_by_four(number):
    return number % 4 == 0


def dividable_by_hundred(number):
    return number % 100 == 0


def dividable_by_four_hundred(number):
    return number % 400 == 0


def check(number):
    number = int(number)

    if not dividable_by_four(number):
        return False

    if not dividable_by_hundred(number):
        return True

    return dividable_by_four_hundred(number)


if __name__ == '__main__':
    print 'True' if check(raw_input()) else 'False'
