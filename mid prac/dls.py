def dls(graph, start, goal, dl):
    visited=[]
    def dfs(node,depth):
        if depth>dl:
            return None
        visited.append(node)
        if(node==goal):
            return f"goal found through path: {visited}"
        for neighbour in graph[node]:
            if neighbour not in visited:
                path=dfs(neighbour,depth+1)
                if path:
                    return path
                
        visited.pop()
        return None
    result = dfs(start,0)
    if result:
        return result
    else:
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
print(dls(tree,'A','I',3))