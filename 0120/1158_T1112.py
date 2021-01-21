import sys
from collections import deque

N, K = map(int,input().split())
circle = deque([i for i in range(1, N + 1)])

ans = []
while circle:
    circle.rotate(1 - K)
    ans.append(str(circle.popleft()))

aa = ', '.join(ans)
print(f'<{aa}>')