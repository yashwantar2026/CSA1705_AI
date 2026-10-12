from collections import deque

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# DFS function
def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


# DIAGRAM 1: Directed graph (nodes 0 to 7)
graph1 = {
    0: [1],
    1: [3],
    2: [1],
    3: [2, 4],
    4: [5],
    5: [7],
    6: [4],
    7: [6]
}

# DIAGRAM 2: Graph (nodes 1 to 8)
graph2 = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 7, 4],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7, 4]
}

# DIAGRAM 3: Tree (nodes 1 to 10)
graph3 = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

# DIAGRAM 4: Graph (nodes 1 to 5)
graph4 = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2, 5],
    5: [2, 4]
}

# Display BFS and DFS for every diagram
diagrams = [
    ("Diagram 1", graph1, 0),
    ("Diagram 2", graph2, 1),
    ("Diagram 3", graph3, 1),
    ("Diagram 4", graph4, 1)
]

for name, graph, start in diagrams:
    print("\n" + name)
    print("BFS:", " -> ".join(map(str, bfs(graph, start))))
    print("DFS:", " -> ".join(map(str, dfs(graph, start))))
