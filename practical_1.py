# simple reflex agent for vacuum cleaner world
#
# algorithm:
# 1. define environment with locations a and b
# 2. set initial location of the vacuum cleaner
# 3. read current location and its dirt status
# 4. if location is dirty, perform suck action
# 5. if location is clean, move to the other location (a -> b or b -> a)
# 6. repeat for given steps and print final environment

def reflex_vacuum_agent(location, status):
    # condition-action rules based on current percept
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'


def run_simulation(initial_location='A', initial_env=None, steps=5):
    if initial_env is None:
        initial_env = {'A': 'Dirty', 'B': 'Dirty'}

    env = initial_env.copy() #shallow copy
    current_location = initial_location

    print("Initial Environment:", env)
    print("Starting Location:", current_location)
    print("-" * 35)

    for step in range(1, steps + 1):
        status = env[current_location]
        action = reflex_vacuum_agent(current_location, status)

        print(f"Step {step}: Location = {current_location}, Status = {status} -> Action = {action}")

        # perform action and update environment
        if action == 'Suck':
            env[current_location] = 'Clean'
        elif action == 'Right':
            current_location = 'B'
        elif action == 'Left':
            current_location = 'A'

    print("-" * 35)
    print("Final Environment:", env)
    print("Final Agent Location:", current_location)


if __name__ == '__main__':
    run_simulation()
