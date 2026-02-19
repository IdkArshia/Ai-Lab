def bfs(graph, start, goal):
    visited = []
    queue = []
    queue.append((start, [start]))
    visited.append(start)

    while queue:
        node, path = queue.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            return

        for neigh in graph[node]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append((neigh, path + [neigh]))

    print("Goal not found")


graph = {
    'Tehran': ['Baghdad', 'Istanbul'],
    'Baghdad': ['Cairo'],
    'Istanbul': ['Berlin'],
    'Cairo': ['Washington'],
    'Berlin': ['Washington'],
    'Washington': []
}

bfs(graph, 'Tehran', 'Washington')
