from collections import deque

# tower of hanoi using state space search (bfs)
#
# algorithm:
# 1. define source (a), auxiliary (b), and destination (c) pegs
# 2. set initial state with all disks on peg a and empty pegs b, c
# 3. push initial state into fifo queue and mark visited
# 4. pop front state from queue
# 5. if all disks are on peg c in order, reconstruct path and stop
# 6. generate all legal disk moves between peg pairs
# 7. for each unvisited successor state, store parent and push to queue
# 8. repeat until goal is reached

def is_goal_state(state, n):
    # goal is all disks on peg C in decreasing order
    return state[2] == tuple(range(n, 0, -1)) and len(state[0]) == 0 and len(state[1]) == 0


def get_legal_successors(state):
    pegs = ['A', 'B', 'C']
    successors = []

    # check all ordered pairs of source and destination pegs
    for from_idx in range(3):
        if not state[from_idx]:
            continue

        disk = state[from_idx][-1]

        for to_idx in range(3):
            if from_idx == to_idx:
                continue

            # check if destination is empty or top disk is larger
            if not state[to_idx] or state[to_idx][-1] > disk:
                new_state = [list(peg) for peg in state]
                new_state[from_idx].pop()
                new_state[to_idx].append(disk)
                next_tuple = tuple(tuple(peg) for peg in new_state)
                move_desc = f"Move disk {disk} from {pegs[from_idx]} to {pegs[to_idx]}"
                successors.append((next_tuple, move_desc))

    return successors


def solve_hanoi_bfs(n=3):
    # state is represented as tuple of tuples: (peg A, peg B, peg C)
    initial_state = (tuple(range(n, 0, -1)), (), ())

    queue = deque([initial_state])
    visited = {initial_state}
    parent = {initial_state: None}
    move_taken = {initial_state: "Initial State"}

    states_explored = 0

    while queue:
        current = queue.popleft()
        states_explored += 1

        if is_goal_state(current, n):
            # reconstruct path from parent pointers
            path = []
            curr = current
            while curr is not None:
                path.append((curr, move_taken[curr]))
                curr = parent[curr]
            path.reverse()
            return path, states_explored

        for successor, move in get_legal_successors(current):
            if successor not in visited:
                visited.add(successor)
                parent[successor] = current
                move_taken[successor] = move
                queue.append(successor)

    return None, states_explored


def print_state(state):
    print(f"  A: {list(state[0])}, B: {list(state[1])}, C: {list(state[2])}")


if __name__ == '__main__':
    disks = 3
    print(f"Solving Tower of Hanoi for {disks} disks using BFS State-Space Search...\n")

    path, states_explored = solve_hanoi_bfs(disks)

    if path:
        print("Sequence of moves:")
        for step, (state, move) in enumerate(path):
            if step == 0:
                print(f"Step {step}: {move}")
            else:
                print(f"Step {step}: {move}")
            print_state(state)

        print("-" * 40)
        print(f"Total legal moves: {len(path) - 1}")
        print(f"Total states explored: {states_explored}")
    else:
        print("No solution found.")
