from cubes import Cube222
import time
import queue
import json


class BruteForceSolver:

    def __init__(self):
        self._cube_format = '000011223344112233445555'
        self._base_color_permutations = ['YRGOBW', 'BRYOWG', 'WRBOGY', 'GRWOYB', 'RWGYBO', 'OYGWBR']
        self._state_dict = {}

    def _apply_color_to_format(self, color_permutation):
        state = self._cube_format
        for i, color in enumerate(color_permutation):
            state = state.replace(str(i), color)
        return state

    def _generate_base_states(self):
        for base_color_permutation in self._base_color_permutations:
            base_states = []
            color_perm = base_color_permutation
            for i in range(4):
                base_states.append(self._apply_color_to_format(color_perm))
                color_perm = color_perm[0] + color_perm[4] + color_perm[1:4] + color_perm[5]
            return base_states

    @staticmethod
    def _inverse_move(move):
        return move + "'" if len(move) == 1 else move[0]

    def generate_state_tree(self, *, log=True):
        if log:
            print('Generating state tree...')
        start_time = time.time()
        progress = 0

        base_states = ['YYYYRRGGOOBBRRGGOOBBWWWW']
        valid_moves = ["R", "R'", "F", "F'", "U", "U'"]  # by natural order
        q = queue.Queue()
        for base_state in base_states:
            q.put((base_state, '', '', 0))

        while not q.empty():
            state, fr, move, depth = q.get()
            if state not in self._state_dict:
                self._state_dict[state] = (fr, move)
                progress += 1
                if log and progress % 10000 == 0:
                    print('States generated: ' + str(progress))
                    print('Current depth: ' + str(depth))
                for valid_move in valid_moves:
                    cube = Cube222(state)
                    cube.make_move(valid_move)
                    q.put((cube.hash(), state, self._inverse_move(valid_move), depth + 1))

        if log:
            end_time = time.time()
            print('Finished in {:.3} seconds'.format(end_time - start_time))
        print(len(self._state_dict.keys()))

    def save_state_tree(self, file_name):
        with open(file_name, mode='w') as file:
            json.dump(self._state_dict, file)

    def load_state_tree(self, file_name):
        with open(file_name, mode='r') as file:
            self._state_dict = json.load(file)


def main():
    solver = BruteForceSolver()
    if input('Do you want to load from an existing json file?(Y/N) ').lower() in ('y', 'yes', 'ye', 'yea', 'yeah'):
        file_name = input('Enter file name: ')
        solver.load_state_tree(file_name)
    else:
        solver.generate_state_tree()
        if input('Do you want to save generated state tree?(Y/N) ').lower() in ('y', 'yes', 'ye', 'yea', 'yeah'):
            file_name = input('Enter file name (with extension): ')
            solver.save_state_tree(file_name)



if __name__ == '__main__':
    main()
