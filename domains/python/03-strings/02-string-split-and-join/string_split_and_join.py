import sys

if __name__ == '__main__':
    splitBySpace = raw_input().split(" ")

    joinByHyphen = "-".join(splitBySpace)

    print joinByHyphen
