def find_parents(x):
    if x==parents[x] :
        return x
    parents[x]=find_parents(parents[x])
    return parents[x]
def union_set(x,y):
    x=find_parents(x)
    y=find_parents(y)
    if x==y : return
    parents[y]=x
    node_count[x]+=node_count[y]

T=int(input())
for TC in range(T):
    parents={}
    node_count={}
    N=int(input())
    for i in range(N):
        A, B=input().split(' ')
        if A not in parents:
            parents[A]=A
            node_count[A]=1
        if B not in parents:
            parents[B]=B
            node_count[B]=1

        if find_parents(A)!=find_parents(B):
            union_set(A,B)
        print(node_count[parents[A]])
