g={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':['H'],'E':[],'F':['I'],'G':[],'H':[],'I':[]}

class AgentDLS:
    def __init__(self,goal,limit):
        self.goal=goal
        self.limit=limit
    def check(self,p):
        if p==self.goal:
            return "done"
        return "search"
    def run_dls(self,g,start):
        seen=[]
        def go(n,d):
            if d>self.limit:
                return None
            seen.append(n)
            print("visit:",n)
            if n==self.goal:
                return "goal found "+self.goal
            for x in g.get(n,[]):
                if x not in seen:
                    r=go(x,d+1)
                    if r:
                        return r
            seen.pop()
            return None
        out=go(start,0)
        if out:
            return out
        return "not found"
    def act(self,p,g):
        if self.check(p)=="done":
            return "goal found"
        else:
            return self.run_dls(g,p)

class Env:
    def __init__(self,data):
        self.data=data
    def sense(self,s):
        return s

st='A'
gl='I'
ag=AgentDLS(gl,3)
e=Env(g)
pp=e.sense(st)
print(ag.act(pp,e.data))
