def divableByFour(number):
    return number % 4 == 0 

def divableByHundred(number):
    return number % 100 == 0 

def divableByFourHundred(number):
    return number % 400 == 0 

def check(number):
    number = int(number)

    if( not divableByFour(number) ):
        return False

    if( not divableByHundred(number) ):
        return True

    return  divableByFourHundred(number)

if __name__ == '__main__':
    print 'True' if check(raw_input()) else 'False'
