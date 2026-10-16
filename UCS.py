
import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor, new_path)
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

uniform_cost_search(graph, 'S', 'G')
