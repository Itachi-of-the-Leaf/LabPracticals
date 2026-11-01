from collections import deque

# breadth first search (bfs) for 8 puzzle problem

INITIAL_STATE = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)


def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c


def get_successors(state):
    row, col = find_blank(state)
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    successors = []

    for dr, dc, move_name in moves:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            # swap blank with neighboring tile
            board = [list(r) for r in state]
            board[row][col], board[new_r][new_c] = board[new_r][new_c], board[row][col]
            new_state = tuple(tuple(r) for r in board)
            successors.append((new_state, move_name))

    return successors


def print_board(state):
    for row in state:
        print(" ".join(str(val) if val != 0 else "_" for val in row))
    print()


def bfs_8_puzzle(start_state, goal_state):
    # fifo queue stores current state
    queue = deque([start_state])
    visited = {start_state}
    parent = {start_state: None}
    action_taken = {start_state: 'Start'}

    nodes_explored = 0

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        # goal check
        if current == goal_state:
            # reconstruct solution path
            path = []
            curr = current
            while curr is not None:
                path.append((curr, action_taken[curr]))
                curr = parent[curr]
            path.reverse()
            return path, nodes_explored

        for successor, move_name in get_successors(current):
            if successor not in visited:
                visited.add(successor)
                parent[successor] = current
                action_taken[successor] = move_name
                queue.append(successor)

    return None, nodes_explored


if __name__ == '__main__':
    print("Initial State:")
    print_board(INITIAL_STATE)
    print("Goal State:")
    print_board(GOAL_STATE)

    path, explored = bfs_8_puzzle(INITIAL_STATE, GOAL_STATE)

    if path:
        print(f"Goal reached in {len(path) - 1} moves (Total nodes explored: {explored}):\n")
        for step, (state, move) in enumerate(path):
            print(f"Step {step} ({move}):")
            print_board(state)
    else:
        print("No solution found.")
