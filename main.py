from copy import deepcopy


class Sticker:
    def __init__(self, color):
        self.color = color

    def set_color(self, new_color):
        self.color = new_color

    def copy_from(self, other_sticker):
        self.color = other_sticker.color

    def __repr__(self):
        return self.color


class Cube222:
    """
           0  1
           2  3
     4  5  6  7  8  9 10 11
    12 13 14 15 16 17 18 19
          20 21
          22 23
    """
    def __init__(self, string):
        self.output_format = '  {}{}\n'\
                             '  {}{}\n'\
                             '{}{}{}{}{}{}{}{}\n'\
                             '{}{}{}{}{}{}{}{}\n'\
                             '  {}{}\n'\
                             '  {}{}'
        self.stickers = [Sticker(i) for i in string]
        self.quads = {
            'R': [
                [7, 21, 18, 1], [15, 23, 10, 3], [8, 16, 17, 9]
            ],
            'L': [
                [6, 0, 19, 20], [14, 2, 11, 22], [4, 12, 13, 5]
            ]
        }

    def copy(self):
        return deepcopy(self)

    def rotate_cw(self, quad):
        t = str(self.stickers[quad[0]])
        self.stickers[quad[0]].copy_from(self.stickers[quad[1]])
        self.stickers[quad[1]].copy_from(self.stickers[quad[2]])
        self.stickers[quad[2]].copy_from(self.stickers[quad[3]])
        self.stickers[quad[3]].set_color(t)

    def rotate_ccw(self, quad):
        t = str(self.stickers[quad[0]])
        self.stickers[quad[0]].copy_from(self.stickers[quad[3]])
        self.stickers[quad[3]].copy_from(self.stickers[quad[2]])
        self.stickers[quad[2]].copy_from(self.stickers[quad[1]])
        self.stickers[quad[1]].set_color(t)

    def make_move(self, move):
        for quad in self.quads[move[0]]:
            if move[-1] == "'":
                self.rotate_ccw(quad)
            else:
                self.rotate_cw(quad)

    def __repr__(self):
        return self.output_format.format(*self.stickers)




def main():
    cube = Cube222('YYYYRRGGOOBBRRGGOOBBWWWW')
    print(cube)
    while True:
        move = input()
        cube.make_move(move)
        print(cube)


if __name__ == '__main__':
    main()
