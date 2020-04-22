from cubes import Cube222
import time


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

    def generate_state_tree(self):
        print('Generating state tree...')
        start_time = time.time()
        base_states = self._generate_base_states()

        end_time = time.time()
        print('Finished in {:.3} seconds'.format(end_time - start_time))


def main():
    solver = BruteForceSolver()
    solver.generate_state_tree()


if __name__ == '__main__':
    main()
