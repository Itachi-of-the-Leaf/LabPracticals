import heapq

# a* algorithm for 8 puzzle problem using misplaced tiles heuristic

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


def count_misplaced(state, goal):
    # count misplaced tiles excluding blank space (0)
    misplaced = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0 and val != goal[r][c]:
                misplaced += 1
    return misplaced


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
            # swap blank with neighbor
            board = [list(r) for r in state]
            board[row][col], board[new_r][new_c] = board[new_r][new_c], board[row][col]
            new_state = tuple(tuple(r) for r in board)
            successors.append((new_state, move_name))

    return successors


def print_board(state):
    for row in state:
        print(" ".join(str(val) if val != 0 else "_" for val in row))
    print()


def a_star_search(start_state, goal_state):
    # priority queue stores (f, g, state_id, state)
    counter = 0
    start_h = count_misplaced(start_state, goal_state)
    start_f = 0 + start_h

    # open list as min-heap
    open_list = []
    heapq.heappush(open_list, (start_f, 0, counter, start_state))

    parent_map = {}
    g_costs = {start_state: 0}

    while open_list:
        f, g, _, current = heapq.heappop(open_list)

        # goal test
        if current == goal_state:
            # reconstruct path
            path = []
            curr = current
            while curr in parent_map:
                prev_state, move_name = parent_map[curr]
                path.append((curr, move_name))
                curr = prev_state
            path.append((start_state, 'Start'))
            path.reverse()
            return path

        for successor, move_name in get_successors(current):
            new_g = g + 1
            if successor not in g_costs or new_g < g_costs[successor]:
                g_costs[successor] = new_g
                h = count_misplaced(successor, goal_state)
                new_f = new_g + h
                counter += 1
                parent_map[successor] = (current, move_name)
                heapq.heappush(open_list, (new_f, new_g, counter, successor))

    return None


if __name__ == '__main__':
    print("Initial State:")
    print_board(INITIAL_STATE)
    print("Goal State:")
    print_board(GOAL_STATE)

    solution = a_star_search(INITIAL_STATE, GOAL_STATE)

    if solution:
        print(f"Goal reached in {len(solution) - 1} moves:\n")
        for step, (state, move) in enumerate(solution):
            g = step
            h = count_misplaced(state, GOAL_STATE)
            f = g + h
            print(f"Step {step} ({move}) | g={g}, h={h}, f={f}:")
            print_board(state)
    else:
        print("No solution found.")
