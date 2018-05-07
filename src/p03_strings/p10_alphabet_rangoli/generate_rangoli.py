class GenerateRangoli():
    def __init__(self):
        pass

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def handle(self, size):
        if size == 0:
            return ''

        if size == 1:
            return self.letters[0]

        rows = size * 2 - 1
        columns = rows * 2 - 1
        x_center = rows / 2
        y_center = columns / 2

        structure = self.create_structure(rows, columns)

        for index in range(size):
            structure = self.stitch_rangoli_line(
                index,
                x_center,
                y_center,
                structure
            )
            print structure


        return self.finalize_rangoli(structure)

    def create_structure(self, rows, columns):
        return [['-' for x in range(columns)] for x in range(rows)]

    def finalize_rangoli(self, structure):
        rangoli = []

        for columns in structure:
            rangoli.append(''.join(columns))

        return '\n'.join(rangoli)

    def stitch_rangoli_line(self, letter, size, x_center, y_center, structure):
        letter = self.letters[size]

        if size == 0:
            structure[x_center][y_center] = letter
            return structure

        y_max_size = x_center * 2

        for index in range(x_center + 1):
            structure[index][y_center + index * 2] = letter
            structure[index][y_center - index * 2] = letter

            structure[y_max_size - index][y_center + index * 2] = letter
            structure[y_max_size - index][y_center - index * 2] = letter

        return structure


def print_rangoli(size):
    generate_rangoli = GenerateRangoli()

    print generate_rangoli.handle(size)
