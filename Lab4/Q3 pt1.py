t={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':['H'],'E':[],'F':['I'],'G':[],'H':[],'I':[]}

def dls_func(node,goal,depth,path):
    if depth==0:
        return False
    path.append(node)
    if node==goal:
        return True
    for ch in t.get(node,[]):
        if dls_func(ch,goal,depth-1,path):
            return True
    path.pop()
    return False

def ids_run(start,goal,maxd):
    for lvl in range(maxd+1):
        p=[]
        if dls_func(start,goal,lvl,p):
            print("found path:",p)
            return
    print("goal not found")

ids_run('A','I',5)