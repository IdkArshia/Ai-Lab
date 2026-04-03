def dfs(tree, start,goal):
    visited=[]
    stack=[]
    visited.append(start)
    stack.append(start)
    while stack:
        node =stack.pop()
        print(f"searching node: {node}")
        if node==goal:
            print("goal reached!")
            return
        for neighbour in reversed(tree[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
    print("goal not found!")

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
start='A'
goal='I'        
dfs(tree,start,goal)