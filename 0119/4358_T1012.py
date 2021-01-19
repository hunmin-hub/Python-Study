import sys

trees={}
N=0
while True :
    tree_name=sys.stdin.readline().rstrip()
    if not tree_name:
        break
    N+=1
    if tree_name not in trees :
        trees[tree_name]=1
    else :
        trees[tree_name]+=1

tree_order=list(trees.keys())
tree_order.sort()
for tree in tree_order :
    answer=trees[tree]/N*100
    print(f'{tree} {answer:.4f}')