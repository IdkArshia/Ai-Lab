import random
cost_matrix = [
[4,6,8,7,5],
[7,5,6,8,4],
[6,4,7,5,8],
[5,8,6,4,7],
[8,6,5,7,4],
[7,4,8,6,5],
[6,7,4,5,8],
[5,6,7,8,4],
[4,7,5,6,8],
[8,5,6,4,7]
]
tasks=10
machines=5
mutation_rate=0.1
generations=100
def make_chrom():
    c=[]
    for i in range(tasks):
        c.append(random.randint(0,machines-1))
    return c
def cost(ch):
    s=0
    for i in range(tasks):
        m=ch[i]
        s+=cost_matrix[i][m]
    return s
def fitness(ch):
    return 1/cost(ch)
def select(pop):
    pop=sorted(pop,key=lambda x:fitness(x),reverse=True)
    return pop[:len(pop)//2]
def cross(p1,p2):
    point=random.randint(1,tasks-2)
    child=p1[:point]+p2[point:]
    return child
def mutate(ch):
    i=random.randint(0,tasks-1)
    ch[i]=random.randint(0,machines-1)
    return ch
def GA(pop_size):
    pop=[]
    for i in range(pop_size):
        pop.append(make_chrom())
    best=None
    best_cost=99999
    best_gen=0
    for g in range(generations):
        pop=sorted(pop,key=lambda x:fitness(x),reverse=True)
        if cost(pop[0])<best_cost:
            best=pop[0]
            best_cost=cost(pop[0])
            best_gen=g
        parents=select(pop)
        new=[]
        while len(new)<pop_size:
            p1,p2=random.sample(parents,2)
            child=cross(p1,p2)
            if random.random()<mutation_rate:
                child=mutate(child)
            new.append(child)
        pop=new
    print("population",pop_size)
    print("best chromosome",best)
    print("cost",best_cost)
    print("fitness",fitness(best))
    print("generation",best_gen)
    print()
GA(10)
GA(30)