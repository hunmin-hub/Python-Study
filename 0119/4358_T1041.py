import sys

trees = {}
n_trees = 0

while True:
    tree = sys.stdin.readline().strip()

    # 더 이상 입력되지 않으면 종료
    if not tree:
        break

    # 종별로 나무 수
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    
    # 총 나무 수
    n_trees += 1

# 출력
for name in sorted(trees.keys()):
    print(f'{name} {trees[name] / n_trees * 100:.4f}')