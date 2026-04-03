def dls(graph, start, goal, dl):
    visited=[]
    def dfs(node,depth):
        if depth>dl:
            return None
        visited.append(node)
        if(node==goal):
            return visited.copy()
        for neighbour in graph[node]:
            if neighbour not in visited:
                path=dfs(neighbour,depth+1)
                if path:
                    return path
                
        visited.pop()
        return None
    return dfs(start,0)
    
def iddls(graph, start,goal,max_depth):
    for d in range(max_depth+1):
        print(f"searching in depth {d}")
        result= dls(graph,start,goal,d)
        if result:
            return f"goal found at depth {d} through path: {result}"
    
    return "goal not found"

                
                
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
print(iddls(tree,'A','F',3))