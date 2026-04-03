class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def bfs_search(self, graph, start, goal):
        visited = []   # List for visited nodes
        queue = []     # Queue for BFS

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)   # Dequeue
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return "Goal not found"

    def act(self, percept, graph):
        if percept==self.goal:
            return f"Goal {self.goal} found!"
        else:
            return self.bfs_search(graph, percept, self.goal)


class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)
    print(action)


# Tree (Graph)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Start & Goal
start_node = 'A'
goal_node = 'I'

# Create objects
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)

# Run
run_agent(agent, environment, start_node)