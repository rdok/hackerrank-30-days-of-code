class StringFormatter:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        output = ''
        min_field_width = len('{0:b}'.format(self.number))

        for index in range(1, self.number + 1):
            output += self.format(index, min_field_width) + '\n'

        return output.rstrip('\n')

    @staticmethod
    def format(number, min_field_width):
        replacement_field = '{0:>{1}} {0:>{1}o} {0:>{1}X} {0:>{1}b}'

        return replacement_field.format(number, min_field_width)
