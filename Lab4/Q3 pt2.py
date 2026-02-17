gr2={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':['H'],'E':[],'F':['I'],'G':[],'H':[],'I':[]}

def dls_graph(n,goal,depth,vis,path):
    if depth<0:
        return False
    vis.add(n)
    path.append(n)
    if n==goal:
        return True
    for nb in gr2.get(n,[]):
        if nb not in vis:
            if dls_graph(nb,goal,depth-1,vis,path):
                return True
    path.pop()
    return False

def ids_graph_run(s,goal,maxd):
    for i in range(maxd+1):
        v=set()
        p=[]
        if dls_graph(s,goal,i,v,p):
            print("path:",p)
            return
    print("not found")

ids_graph_run('A','I',5)