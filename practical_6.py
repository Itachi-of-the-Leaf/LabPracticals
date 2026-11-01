# depth first search (dfs) for water jug problem
#
# algorithm:
# 1. define jug capacities (4l and 3l) and goal state (2l in any jug)
# 2. initialize stack and visited set with initial state (0, 0)
# 3. pop top state from stack
# 4. if goal state reached, trace back path using parents and stop
# 5. generate valid next states (fill, empty, pour between jugs)
# 6. push unvisited successors onto stack
# 7. repeat until goal is reached or stack is empty

CAPACITY_A = 4
CAPACITY_B = 3


def is_goal(state):
    # goal is 2 litres in either jug
    return state[0] == 2 or state[1] == 2


def get_successors(state):
    x, y = state
    moves = []

    # 1. fill 4-litre jug
    if x < CAPACITY_A:
        moves.append(((CAPACITY_A, y), "Fill 4L jug"))

    # 2. fill 3-litre jug
    if y < CAPACITY_B:
        moves.append(((x, CAPACITY_B), "Fill 3L jug"))

    # 3. empty 4-litre jug
    if x > 0:
        moves.append(((0, y), "Empty 4L jug"))

    # 4. empty 3-litre jug
    if y > 0:
        moves.append(((x, 0), "Empty 3L jug"))

    # 5. pour 4L jug into 3L jug
    if x > 0 and y < CAPACITY_B:
        pour = min(x, CAPACITY_B - y)
        moves.append(((x - pour, y + pour), "Pour 4L into 3L"))

    # 6. pour 3L jug into 4L jug
    if y > 0 and x < CAPACITY_A:
        pour = min(y, CAPACITY_A - x)
        moves.append(((x + pour, y - pour), "Pour 3L into 4L"))

    return moves


def dfs_water_jug():
    initial_state = (0, 0)

    # lifo stack for dfs
    stack = [initial_state]
    visited = {initial_state}
    parent = {initial_state: None}
    action_taken = {initial_state: "Initial State"}

    while stack:
        current = stack.pop()

        if is_goal(current):
            # reconstruct path
            path = []
            curr = current
            while curr is not None:
                path.append((curr, action_taken[curr]))
                curr = parent[curr]
            path.reverse()
            return path

        # generate valid next states
        for successor, action in get_successors(current):
            if successor not in visited:
                visited.add(successor)
                parent[successor] = current
                action_taken[successor] = action
                stack.append(successor)

    return None


if __name__ == '__main__':
    print(f"Solving Water Jug Problem (Capacities: {CAPACITY_A}L and {CAPACITY_B}L) using DFS...\n")

    path = dfs_water_jug()

    if path:
        print("Sequence of actions to reach 2 litres:")
        for step, (state, action) in enumerate(path):
            print(f"Step {step}: {action:<20} -> Jug 4L: {state[0]}L, Jug 3L: {state[1]}L")
        print("-" * 50)
        print(f"Total steps: {len(path) - 1}")
    else:
        print("No solution found.")
