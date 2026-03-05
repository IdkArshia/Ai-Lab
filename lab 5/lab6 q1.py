import heapq

graph = {
'S':[('A',2),('B',5),('C',4)],
'A':[('D',7),('E',3)],
'B':[('F',6)],
'C':[('G',2)],
'D':[('T',4)],
'E':[('T',6)],
'F':[('T',5)],
'G':[('T',3)],
'T':[]
}

def beam_search(start,goal,k):
    beam=[(0,[start])]
    while len(beam)>0:
        new_paths=[]
        for item in beam:
            cost=item[0]
            path=item[1]
            node=path[-1]
            if node==goal:
                return path,cost
            for n,c in graph[node]:
                p=path+[n]
                new_paths.append((cost+c,p))
        beam=heapq.nsmallest(k,new_paths,key=lambda x:x[0])
    return None,None
for k in [1,2,3]:
    p,c=beam_search('S','T',k)
    print("k =",k)
    print("path =",p)
    print("cost =",c)
    print()