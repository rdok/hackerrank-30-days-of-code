class StringFormatter:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        min_field_width = len(bin(self.number))

        replacement_field = '{0:>{4}} {1:>{4}} {2:>{4}} {3:>{4}}'

        return replacement_field.format(
            self.number,
            oct(self.number),
            hex(self.number),
            bin(self.number),
            min_field_width
        )

    @staticmethod
    def format(number):
        min_field_width = len('{0:b}'.format(number))

        replacement_field = ' {0:>{1}} {0:>{1}o} {0:>{1}x} {0:>{1}b}'

        return replacement_field.format(number, min_field_width)
