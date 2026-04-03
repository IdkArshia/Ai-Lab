def bfs(tree, start, goal):
    visited=[]
    queue=[]
    visited.append(start)
    queue.append(start)
    while queue:
        node=queue.pop(0)
        if(node==goal):
            print("goal reached!")
            break
        for neighbour in tree[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
