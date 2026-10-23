
import heapq

def gbfs(graph, heuristic, start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Path:", " -> ".join(path))
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    print("Goal not reachable")


graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 2), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

heuristic = {
    'S': 4,
    'A': 3,
    'B': 3,
    'C': 2,
    'D': 3,
    'G': 0
}

gbfs(graph, heuristic, 'S', 'G')
