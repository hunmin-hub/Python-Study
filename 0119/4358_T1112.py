import sys

tree_encyclopedia = {}
tree_count = 0

while True:
    tree = sys.stdin.readline().rstrip()
    
    if not tree:
        break
    
    tree_encyclopedia[tree] = tree_encyclopedia.get(tree,0) + 1
    tree_count += 1
    

for tree, count in sorted(tree_encyclopedia.items()):
    print(f'{tree} {count / tree_count * 100:.4f}')