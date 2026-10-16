
import heapq

def a_star_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f_cost, g_cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g_cost)
            return

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_g = g_cost + edge_cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
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

# Example heuristic values (estimated costs to reach G)
heuristic = {
    'S': 4,
    'A': 3,
    'B': 3,
    'C': 2,
    'D': 3,
    'G': 0
}

a_star_search(graph, heuristic, 'S', 'G')
