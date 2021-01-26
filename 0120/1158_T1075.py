import sys

n, k = map(int, sys.stdin.readline().strip().split())

arr = [i for i in range(1, n + 1)]
ret = []
i = 0

for _ in range(n):
    i = (i + (k - 1)) % len(arr)
    ret.append(str(arr.pop(i)))

print(f"<{', '.join(ret)}>")