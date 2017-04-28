def executeCommands():
    numberOfCommands = int( raw_input() )

    if( numberOfCommands == 0):
        return None

    lists = []

    for commandIndex in range(0, numberOfCommands):
        rawCommand = raw_input().split(' ')
        lists.rawCommand[0]()


    print lists

if __name__ == '__main__':
    executeCommands()
