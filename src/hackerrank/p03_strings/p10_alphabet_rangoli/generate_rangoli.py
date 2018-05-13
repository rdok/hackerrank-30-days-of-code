class GenerateRangoli():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def handle(self, size):
        frame = self.create_frame(size)
        canvas = self.create_canvas(frame['width'], frame['height'])

        for index in range(size):
            character = self.letters[size  - 1]

            canvas = self.stitch_rangoli_line(
                character,
                index  - 1,
                frame['x_center'],
                frame['y_center'],
                canvas
            )

        return self.convert_to_text(canvas)

    def create_frame(self, size):
        response = {"height": size, "width": size, "x_center": 0, "y_center": 0}

        if size <= 1:
            return response

        response["height"] = size * 2 - 1
        response["width"] = response["height"] * 2 - 1
        response["x_center"] = 2 * size - 2
        response["y_center"] = size - 1

        return response

    def create_canvas(self, rows, columns):
        return [['-' for x in range(rows)] for x in range(columns)]

    def convert_to_text(self, structure):
        rangoli = []

        for columns in structure:
            rangoli.append(''.join(columns))

        return '\n'.join(rangoli)

    def stitch_rangoli_line(self, character, size, x_center, y_center, structure):

        if size == 0:
            structure[x_center][y_center] = character
            return structure

        y_max_size = y_center * 2

        for index in range(x_center + 1):
            structure[index][y_center + index * 2] = character
            structure[index][y_center - index * 2] = character

            print y_max_size

            structure[y_max_size - index][y_center + index * 2] = character
            structure[y_max_size - index][y_center - index * 2] = character

        return structure


def print_rangoli(size):
    generate_rangoli = GenerateRangoli()

    print generate_rangoli.handle(size)
