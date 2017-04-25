def divableByFour(number):
    return number % 4 == 0 

def divableByHundred(number):
    return number % 100 == 0 

def divableByFourHundred(number):
    return number % 400 == 0 

def check(number):
    number = int(number)
    return divableByFour(number) and divableByHundred(number) and divableByFourHundred(number)

if __name__ == '__main__':
    print 'True' if check(raw_input()) else 'False'
