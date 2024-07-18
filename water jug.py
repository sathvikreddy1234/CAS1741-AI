def water_jug_problem(jug1, jug2, goal):
    queue = deque([(0, 0, [])])  # (jug1, jug2, steps)
    visited = set((0, 0))

    while queue:
        j1, j2, steps = queue.popleft()
        if j1 == goal or j2 == goal:
            return steps + [(j1, j2)]

        for j1_new, j2_new in [
            (jug1, 0),  # empty jug1
            (0, jug2),  # empty jug2
            (0, 0),  # fill both jugs
            (jug1, j2 - jug1),  # pour jug1 into jug2
            (j1 - jug2, jug2)  # pour jug2 into jug1
        ]:
            if (j1_new, j2_new) not in visited:
                queue.append((j1_new, j2_new, steps + [(j1, j2)]))
                visited.add((j1_new, j2_new))

    return None
jug1 = 3
jug2 = 5
goal = 4
solution = water_jug_problem(jug1, jug2, goal)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
