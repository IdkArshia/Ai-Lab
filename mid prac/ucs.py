def ucs(graph, start, goal):
    frontier=[(start,0)]
    visited=set()
    cost_so_far={start:0}
    came_from={start:None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        node,cost=frontier.pop(0)
        if node in visited:
            continue
        visited.add(node)
        if node== goal:
            path=[]
            while node is not None:
                path.append(node)
                node=came_from[node]
            path.reverse()
            print(f"goal found! path: {path}, cost: {cost}")
            return
        for neighbour,c in graph[node].items():
            nc=cost+c
            if neighbour not in cost_so_far or nc< cost_so_far[neighbour]:
                cost_so_far[neighbour]=nc
                came_from[neighbour]=node
                frontier.append((neighbour,nc))
    print("goal not found")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {},
    'E': {},
    'F': {}
}
ucs(graph,'A','F')