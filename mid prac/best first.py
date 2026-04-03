from queue import PriorityQueue
def bfs(graph, start,goal):
    visited=set()
    pq=PriorityQueue()
    pq.put((0,start))
    while not pq.empty():
        cost,node=pq.get()
        if node not in visited:
            visited.add(node)
            if node==goal:
                print(f"goal found! path: {visited}")
                return True
            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    pq.put((weight,neighbour))
    print("goal not found")
    return False

print("best first search path: ")
graph = {
'S': [('A', 3), ('B', 6), ('C', 5)],
'A': [('D', 9), ('E', 8)],
'B': [('F', 12),
('G', 14)],
'C': [('H', 7)],
'H': [('I', 5),
('J', 6)],
'I': [('K', 1),
('L', 10), ('M', 2)],
'D': [],'E': [],
'F': [],'G': [],
'J': [],'K': [],
'L': [],'M': []
}
bfs(graph,'S','I')