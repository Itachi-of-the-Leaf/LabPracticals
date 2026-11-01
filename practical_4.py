import random

# local beam search for travelling salesman problem (tsp)

CITIES = ['A', 'B', 'C', 'D', 'E', 'F']

# distance matrix from practical manual
DISTANCE_MATRIX = [
    [0, 10, 15, 20, 18, 12],
    [10, 0, 35, 25, 17, 28],
    [15, 35, 0, 30, 28, 20],
    [20, 25, 30, 0, 22, 16],
    [18, 17, 28, 22, 0, 14],
    [12, 28, 20, 16, 14, 0]
]


def calculate_tour_cost(tour):
    total = 0
    num_cities = len(tour)
    # sum edge costs and return edge to start
    for i in range(num_cities):
        from_city = tour[i]
        to_city = tour[(i + 1) % num_cities]
        total += DISTANCE_MATRIX[from_city][to_city]
    return total


def generate_neighbors(tour):
    # 2-opt neighbourhood generation
    neighbors = []
    num_cities = len(tour)
    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            # reverse segment between i and j
            new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
            neighbors.append(tuple(new_tour))
    return neighbors


def format_tour(tour):
    names = [CITIES[idx] for idx in tour]
    return " -> ".join(names + [names[0]])


def local_beam_search(beam_width=4, max_iterations=20, patience=5, random_seed=42):
    random.seed(random_seed)
    num_cities = len(CITIES)

    # generate k random initial tours starting with city 0
    beam = set()
    while len(beam) < beam_width:
        other_cities = list(range(1, num_cities))
        random.shuffle(other_cities)
        candidate = (0,) + tuple(other_cities)
        beam.add(candidate)

    beam = list(beam)
    global_best_tour = min(beam, key=calculate_tour_cost)
    global_best_cost = calculate_tour_cost(global_best_tour)
    best_iteration = 0
    no_improvement_count = 0

    print(f"Initial Beam (k = {beam_width}):")
    for tour in beam:
        print(f"  Tour: {format_tour(tour)} | Cost: {calculate_tour_cost(tour)}")
    print(f"Initial Global Best Cost: {global_best_cost}\n")

    for iteration in range(1, max_iterations + 1):
        # generate all unique neighbours for each candidate in beam
        successor_pool = set()
        for tour in beam:
            for neighbor in generate_neighbors(tour):
                successor_pool.add(neighbor)

        # sort successors by cost
        sorted_successors = sorted(successor_pool, key=calculate_tour_cost)

        # pick top k successors for next beam
        beam = sorted_successors[:beam_width]

        current_best = beam[0]
        current_best_cost = calculate_tour_cost(current_best)

        # update global best
        if current_best_cost < global_best_cost:
            global_best_cost = current_best_cost
            global_best_tour = current_best
            best_iteration = iteration
            no_improvement_count = 0
        else:
            no_improvement_count += 1

        print(f"Iteration {iteration}: Current Best = {current_best_cost}, Global Best = {global_best_cost}")

        # stop if no improvement occurs for specified number of iterations
        if no_improvement_count >= patience:
            print(f"\nSearch stopped: no improvement for {patience} iterations.")
            break

    return global_best_tour, global_best_cost, best_iteration


if __name__ == '__main__':
    print("Distance Matrix for Cities [A, B, C, D, E, F]:")
    for row in DISTANCE_MATRIX:
        print(row)
    print("-" * 50)

    best_tour, best_cost, found_at = local_beam_search(beam_width=4, max_iterations=15, random_seed=10)

    print("-" * 50)
    print("Final Result:")
    print(f"Best Tour Found: {format_tour(best_tour)}")
    print(f"Total Distance: {best_cost}")
    print(f"Found at Iteration: {found_at}")
