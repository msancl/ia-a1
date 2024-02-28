"""
Name of the author(s):
- Charles Lohest <charles.lohest@uclouvain.be>
"""
import time
import sys
from search import *


#################
# Problem class #
#################
dico = {}
class Pacman(Problem):

    def find_pacman(self, state):
        # Finds pacman and returns the position in the grid

        
        for i, row in enumerate(state.grid):
            for j, cell in enumerate(row):
                if cell == 'P':  # Pacman found
                    return (i, j) 

    def actions(self, state):
        actions = []
        grid = state.grid
        pacman_pos = self.find_pacman(state)
        max_x = state.shape(0)
        max_y = state.shape(1)

        directions = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1),}
        







    def result(self, state, action):
        # Apply the action to the state and return the new state
        pass
        
    def goal_test(self, state):
    	#check for goal state
        if state.answer == 0:
            return True
        return False



###############
# State class #
###############
class State:

    def __init__(self, shape, grid, answer=None, move="Init"):
        self.shape = shape
        self.answer = answer
        self.grid = grid
        self.move = move

    def __str__(self):
        s = self.move + "\n"
        for line in self.grid:
            s += "".join(line) + "\n"
        return s


def read_instance_file(filepath):
    with open(filepath) as fd:
        lines = fd.read().splitlines()
    shape_x, shape_y = tuple(map(int, lines[0].split()))
    initial_grid = [tuple(row) for row in lines[1:1 + shape_x]]
    initial_fruit_count = sum(row.count('F') for row in initial_grid)

    return (shape_x, shape_y), initial_grid, initial_fruit_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./Pacman.py <path_to_instance_file>")
    filepath = sys.argv[1]

    shape, initial_grid, initial_fruit_count = read_instance_file(filepath)
    #print(read_instance_file(filepath))
    initial_grid2 = [('.', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '.'), ('.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.'), ('.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.', '.'), ('.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.'), ('.', '#', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.'), ('.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'), ('.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'), ('.', '#', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.'), ('.', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.')]
    init_state = State(shape, tuple(initial_grid), initial_fruit_count, "Init")
    #print(str(init_state))
    
    problem = Pacman(init_state)

    print(problem.find_pacman(problem.initial))
    
    """

    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = breadth_first_tree_search(problem)
    end_timer = time.perf_counter()

    # Example of print
    path = node.path()

    for n in path:
        # assuming that the __str__ function of state outputs the correct format
        print(n.state)

    print("* Execution time:\t", str(end_timer - start_timer))
    print("* Path cost to goal:\t", node.depth, "moves")
    print("* #Nodes explored:\t", nb_explored)
    print("* Queue size at goal:\t",  remaining_nodes)"""
