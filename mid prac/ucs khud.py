def ucs(graph, start, goal):
    # Initialize
    frontier = [(start, 0)]   # (node, cost)
    visited = set()
    cost_so_far = {start: 0}
    came_from = {start: None}

    while frontier:
        # Sort by cost (acts like priority queue)
        frontier.sort(key=lambda x: x[1])

        # Get lowest cost node
        current_node, current_cost = frontier.pop(0)

        # Skip if already visited
        if current_node in visited:
            continue

        visited.add(current_node)

        # Goal check
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            print(f"Goal found with UCS. Path: {path}, Total Cost: {current_cost}")
            return

        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found") 