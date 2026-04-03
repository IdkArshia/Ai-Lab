from queue import PriorityQueue

graph = {
    "T0": {"T1": 1, "T2": 1},
    "T1": {"T3": 1, "T4": 1},
    "T2": {"T5": 1},
    "T3": {"T6": 1},
    "T4": {"T6": 1},
    "T5": {"T6": 1},
    "T6": {},
}

heuristics = {
    "T0": 5,
    "T1": 3,
    "T2": 4,
    "T3": 2,
    "T4": 1,
    "T5": 2,
    "T6": 0,
}

class Node:
    def __init__(self, task):
        self.task = task
        self.h = heuristics[task]

    def __lt__(self, other):
        return self.h < other.h


def bfsa(graph, heuristics, start):
    # 🔁 Build reverse graph (dependency → tasks)
    reverse_graph = {t: [] for t in graph}
    for task in graph:
        for dep in graph[task]:
            reverse_graph[dep].append(task)

    pq = PriorityQueue()
    pq.put(Node(start))

    visited = set()
    path = []

    while not pq.empty():
        cn = pq.get()
        current = cn.task

        if current in visited:
            continue

        visited.add(current)
        path.append(current)

        # Find tasks unlocked by this one
        for neighbor in reverse_graph[current]:
            if neighbor not in visited:
                pq.put(Node(neighbor))

    print("Path followed:", path)


bfsa(graph, heuristics, 'T6')