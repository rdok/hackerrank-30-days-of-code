if __name__ == '__main__':
    user_input = raw_input()

    print any(char.isalnum() for char in user_input)
    print any(char.isalpha() for char in user_input)
    print any(char.isdigit() for char in user_input)
    print any(char.islower() for char in user_input)
    print any(char.isupper() for char in user_input)
