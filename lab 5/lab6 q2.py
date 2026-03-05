import random

def f(x):
    return -x*x + 10*x + 5
def hill():
    x=random.randint(0,100)
    while True:
        cur=f(x)
        best=x
        if x-1>=0:
            if f(x-1)>cur:
                best=x-1
                cur=f(x-1)
        if x+1<=100:
            if f(x+1)>cur:
                best=x+1
                cur=f(x+1)
        if best==x:
            break
        x=best
    return x,f(x)
for i in range(5):
    ans=hill()
    print("run",i+1)
    print("x =",ans[0])
    print("value =",ans[1])
    print()