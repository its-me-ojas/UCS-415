# 8 puzzle problem
import copy

initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[2, 8, 1], [0, 4, 1], [7, 6, 5]]


# find empty block
def find_empty_block(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)


# find whether to move left, right, up or down
def find_move(initial_state):
    if find_empty_block(initial_state) == (0, 0):
        move = ["right", "down"]
    elif find_empty_block(initial_state) == (0, 1):
        move = ["left", "right", "down"]
    elif find_empty_block(initial_state) == (0, 2):
        move = ["left", "down"]
    elif find_empty_block(initial_state) == (1, 0):
        move = ["up", "right", "down"]
    elif find_empty_block(initial_state) == (1, 1):
        move = ["left", "up", "right", "down"]
    elif find_empty_block(initial_state) == (1, 2):
        move = ["left", "up", "down"]
    elif find_empty_block(initial_state) == (2, 0):
        move = ["up", "right"]
    elif find_empty_block(initial_state) == (2, 1):
        move = ["left", "up", "right"]
    elif find_empty_block(initial_state) == (2, 2):
        move = ["left", "up"]
    return move


def move_right(state):

    i, j = find_empty_block(state)
    state[i][j] = state[i][j + 1]
    state[i][j + 1] = 0
    return state


def move_left(state):
    i, j = find_empty_block(state)
    state[i][j] = state[i][j - 1]
    state[i][j - 1] = 0
    return state


def move_up(state):
    i, j = find_empty_block(state)
    state[i][j] = state[i - 1][j]
    state[i - 1][j] = 0
    return state


def move_down(state):
    i, j = find_empty_block(state)
    state[i][j] = state[i + 1][j]
    state[i + 1][j] = 0
    return state


def print_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=" ")
        print()


# main logic to solve the puzzle
def eight_puzzle_problem(initial_state, goal_state, copy_state):
    if initial_state == goal_state:
        print("yay goal reached")
        return
    else:
        print("Initial state is not same as goal state")
        print("Initial state:")
        print_state(initial_state)
        move = find_move(initial_state)
        for i in move:
            if i == "right":
                right_state = move_right(initial_state)
                if tuple(map(tuple, right_state)) in copy_state:
                    print("Already visited")
                    continue
                copy_state.add(tuple(map(tuple, right_state)))
                eight_puzzle_problem(right_state, goal_state, copy_state)
            elif i == "left":
                left_state = move_left(initial_state)
                if tuple(map(tuple, left_state)) in copy_state:
                    print("Already visited")
                    continue
                copy_state.add(tuple(map(tuple, left_state)))
                eight_puzzle_problem(left_state, goal_state, copy_state)
            elif i == "up":
                up_state = move_up(initial_state)
                if tuple(map(tuple, up_state)) in copy_state:
                    print("Already visited")
                    continue
                copy_state.add(tuple(map(tuple, up_state)))
                eight_puzzle_problem(up_state, goal_state, copy_state)
            elif i == "down":
                down_state = move_down(initial_state)
                if tuple(map(tuple, down_state)) in copy_state:
                    print("Already visited")
                    continue
                copy_state.add(tuple(map(tuple, down_state)))
                eight_puzzle_problem(down_state, goal_state, copy_state)


copy_state = set()
eight_puzzle_problem(initial_state, goal_state, copy_state)
