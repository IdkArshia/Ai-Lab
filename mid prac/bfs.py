tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H'],
    'E':[],
    'F':['I'],
    'G':[],
    'H':[],
    'I':[]
}

def bfs(start, goal, tree):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)

    while queue:
        node=queue.pop(0)
        print('Node: ',node)
        if node==goal:
            print('Goal reached!')
            break
        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

start='A'
goal='I'

print('following is the bfs:')
bfs(start,goal,tree)