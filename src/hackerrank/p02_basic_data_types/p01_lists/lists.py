lists = []


def execute_commands():
    number_of_commands = int(raw_input())
    available_commands = {
        'print': print_list,
        'insert': insert_list,
        'remove': remove_list,
        'append': append_list,
        'sort': sort_list,
        'pop': pop_list,
        'reverse': reverse_list
    }

    for commandIndex in range(0, number_of_commands):
        raw_command = raw_input().split(' ')

        if not (raw_command[1:]):
            available_commands[raw_command[0]]()
        else:
            arguments = raw_command[1:]
            available_commands[raw_command[0]](*arguments)


def print_list():
    print lists


def insert_list(index, value):
    index = int(index)
    value = int(value)

    lists.insert(index, value)


def remove_list(value):
    number = int(value)
    lists.remove(number)


def append_list(value):
    number = int(value)
    lists.append(number)


def sort_list():
    lists.sort()


def pop_list():
    lists.pop()


def reverse_list():
    lists.reverse()


if __name__ == '__main__':
    execute_commands()
