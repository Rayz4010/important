from collections import deque

initial_state = {'left': (3, 3), 'right': (0, 0), 'boat': 'left'}
goal_state = {'left': (0, 0), 'right': (3, 3), 'boat': 'right'}

def is_valid(state):
    left_m, left_c = state['left']
    right_m, right_c = state['right']
    if left_m < 0 or left_c < 0 or right_m < 0 or right_c < 0:
        return False
    if left_m > 3 or left_c > 3 or right_m > 3 or right_c > 3:
        return False
    if left_m < left_c and left_m > 0:
        return False
    if right_m < right_c and right_m > 0:
        return False
    return True

def generate_next_states(current_state):
    next_states = []
    for i in range(3):
        for j in range(3):
            if i + j > 2 or i + j == 0:
                continue
            if current_state['boat'] == 'left':
                new_state = {
                    'left': (current_state['left'][0] - i, current_state['left'][1] - j),
                    'right': (current_state['right'][0] + i, current_state['right'][1] + j),
                    'boat': 'right'
                }
            else:
                new_state = {
                    'left': (current_state['left'][0] + i, current_state['left'][1] + j),
                    'right': (current_state['right'][0] - i, current_state['right'][1] - j),
                    'boat': 'left'
                }
            if is_valid(new_state):
                next_states.append(new_state)
    return next_states

def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        if tuple(current_state['left'] + current_state['right'] + (current_state['boat'],)) in visited:
            continue
        visited.add(tuple(current_state['left'] + current_state['right'] + (current_state['boat'],)))
        for next_state in generate_next_states(current_state):
            queue.append((next_state, path + [next_state]))

    return None

solution = bfs(initial_state, goal_state)

if solution:
    print("Solution found with", len(solution), "steps:")
    for i, state in enumerate(solution):
        print("Step", i + 1, ":", state)
else:
    print("No solution found.")