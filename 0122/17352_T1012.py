import sys
sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline().rstrip())
parents=[x for x in range(0,N+1)]
def find_parents(x) :
    if x==parents[x] :
        return x
    parents[x]=find_parents(parents[x])
    return parents[x]

def union_find(x,y) :
    x=find_parents(x)
    y=find_parents(y)
    if x==y :
        return
    parents[y]=x

for _ in range(0,N-2) :
    a, b=map(int,sys.stdin.readline().rstrip().split(' ')) # a to b : a->b
    if find_parents(a)!=find_parents(b) :
        union_find(a,b)

answer_x=find_parents(1)
for i in range(2,N+1) :
    if answer_x!=find_parents(i) :
        print("1",i)
        break
