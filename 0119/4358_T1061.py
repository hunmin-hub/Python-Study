import sys
dic = {}
cnt = 0

while(True):
    treeName = sys.stdin.readline().rstrip()
    if not treeName:
        break
    if treeName in dic:
        dic[treeName] += 1
    else:
        dic[treeName] = 1
    cnt += 1
answer = sorted(dic.items(), key=(lambda x: x[0]))
for tree in answer:
    print(f'{tree[0]} {(tree[1]/cnt*100):.4f}')
