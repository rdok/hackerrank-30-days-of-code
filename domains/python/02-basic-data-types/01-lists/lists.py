import sys
lists = []

def executeCommands():
    numberOfCommands = int( raw_input() )
    availableCommands = {
        'print': printList,
        'insert': insertList,
        'remove': removeList,
        'append': appendList,
        'sort': sortList,
        'pop': popList,
        'reverse': reverseList
    }

    for commandIndex in range(0, numberOfCommands):
        rawCommand = raw_input().split(' ')
        
        if not ( rawCommand[1:] ) :
            availableCommands[ rawCommand[0] ]()
        else:
            arguments = rawCommand[1:]
            availableCommands[ rawCommand[0] ]( *arguments )

def printList(): 
    print lists

def insertList(index, value): 
    index = int( index )
    value = int( value )

    lists.insert(index, value)

def removeList(value): 
    number = int( value )
    lists.remove(number)

def appendList(value): 
    number = int( value )
    lists.append(number)

def sortList(): 
    lists.sort()

def popList(): 
    lists.pop()

def reverseList(): 
    lists.reverse()

if __name__ == '__main__':
    executeCommands()
