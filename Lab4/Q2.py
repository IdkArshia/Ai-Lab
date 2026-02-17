import itertools

names=['A','B','C','D']
d={('A','B'):10,('A','C'):15,('A','D'):20,
   ('B','A'):10,('B','C'):35,('B','D'):25,
   ('C','A'):15,('C','B'):35,('C','D'):30,
   ('D','A'):20,('D','B'):25,('D','C'):30}

def solve_tsp(start):
    left=[i for i in names if i!=start]
    best_cost=999999
    best_route=None
    for perm in itertools.permutations(left):
        route=[start]+list(perm)+[start]
        total=0
        for i in range(len(route)-1):
            total+=d[(route[i],route[i+1])]
        if total<best_cost:
            best_cost=total
            best_route=route
    return best_route,best_cost

r,c=solve_tsp('A')
print("route:",r)
print("cost:",c)
