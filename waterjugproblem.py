from collections import deque

def water_jug():
    capacity = (3, 5, 8)
    start = (0, 0, 8)
    goal = (0, 4, 4)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            for step in path + [state]:
                print(step)
            return

        if state in visited:
            continue

        visited.add(state)

        for i in range(3):
            for j in range(3):
                if i != j:
                    amount = min(state[i], capacity[j] - state[j])

                    if amount > 0:
                        new_state = list(state)
                        new_state[i] -= amount
                        new_state[j] += amount
                        new_state = tuple(new_state)

                        if new_state not in visited:
                            queue.append((new_state, path + [state]))

    print("Solution not found")

water_jug()
