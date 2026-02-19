def ucs(graph, start, goal):
    frontier = [(start, 0, [start])]
    visited = []
    cost_map = {start: 0}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        node, cost, path = frontier.pop(0)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            print("Cheapest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for neigh in graph[node]:
            new_cost = cost + graph[node][neigh]

            if neigh not in cost_map or new_cost < cost_map[neigh]:
                cost_map[neigh] = new_cost
                frontier.append((neigh, new_cost, path + [neigh]))

    print("Goal not found")


graph = {
    'Earth': {'Moon_Base': 10, 'Orbital_Platform': 5},
    'Orbital_Platform': {'Moon_Base': 2, 'Mars': 60},
    'Moon_Base': {'Mars': 50},
    'Mars': {}
}

ucs(graph, 'Earth', 'Mars')
