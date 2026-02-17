wg={'A':{'B':2,'C':1},'B':{'D':4,'E':3},'C':{'F':1,'G':5},'D':{'H':2},'E':{},'F':{'I':6},'G':{},'H':{},'I':{}}

class AgentUCS:
    def __init__(self,goal):
        self.goal=goal
    def search(self,gr,start):
        q=[(start,0)]
        done=set()
        parent={start:None}
        cost_map={start:0}
        while q:
            q.sort(key=lambda k:k[1])
            cur,cc=q.pop(0)
            if cur in done:
                continue
            done.add(cur)
            print("node:",cur,"cost:",cc)
            if cur==self.goal:
                path=[]
                while cur!=None:
                    path.append(cur)
                    cur=parent[cur]
                path.reverse()
                return path,cc
            for nb,w in gr[cur].items():
                nc=cc+w
                if nb not in cost_map or nc<cost_map[nb]:
                    cost_map[nb]=nc
                    parent[nb]=cur
                    q.append((nb,nc))
        return "no path"
    def act(self,start,gr):
        return self.search(gr,start)

a2=AgentUCS('I')
print(a2.act('A',wg))
