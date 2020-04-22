from copy import deepcopy


class InvalidMoveNotationError(Exception):
    def __init__(self, move, *args) -> None:
        self.move = move
        super().__init__(move, *args)

    def __str__(self):
        return 'Invalid move "' + self.move + '"'


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
        self._output_format = '   {}{}\n' \
                              '   {}{}\n' \
                              '{}{} {}{} {}{} {}{}\n' \
                              '{}{} {}{} {}{} {}{}\n' \
                              '   {}{}\n' \
                              '   {}{}'
        self._stickers = [*string]
        self._quads = {
            'R': [
                [7, 21, 18, 1], [15, 23, 10, 3], [8, 16, 17, 9]
            ],
            'L': [
                [6, 0, 19, 20], [14, 2, 11, 22], [4, 12, 13, 5]
            ],
            'F': [
                [2, 13, 21, 8], [3, 5, 20, 16], [6, 14, 15, 7]
            ],
            'B': [
                [0, 9, 23, 12], [1, 17, 22, 4], [10, 18, 19, 11]
            ],
            'U': [
                [6, 8, 10, 4], [7, 9, 11, 5], [0, 2, 3, 1]
            ],
            'D': [
                [14, 12, 18, 16], [15, 13, 19, 17], [20, 22, 23, 21]
            ]
        }

    def copy(self):
        return deepcopy(self)

    def _rotate_cw(self, quad):
        s = self._stickers
        s[quad[0]], s[quad[1]], s[quad[2]], s[quad[3]] = s[quad[1]], s[quad[2]], s[quad[3]], s[quad[0]]

    def _rotate_ccw(self, quad):
        s = self._stickers
        s[quad[0]], s[quad[3]], s[quad[2]], s[quad[1]] = s[quad[3]], s[quad[2]], s[quad[1]], s[quad[0]]

    def make_move(self, move: str):
        if (not 0 < len(move) < 3) or move[0] not in self._quads or (len(move) == 2 and move[1] not in "'2"):
            raise InvalidMoveNotationError(move)
        for quad in self._quads[move[0]]:
            if move[-1] == "'":
                self._rotate_ccw(quad)
            elif move[-1] == "2":
                self._rotate_cw(quad)
                self._rotate_cw(quad)
            else:
                self._rotate_cw(quad)

    def make_moves(self, moves: str):
        for move in moves.split(' '):
            self.make_move(move)

    def __repr__(self):
        return self._output_format.format(*self._stickers)


def main():
    cube = Cube222('YYYYRRGGOOBBRRGGOOBBWWWW')
    print(cube)
    while True:
        moves = input()
        cube.make_moves(moves)
        print(cube)


if __name__ == '__main__':
    main()
