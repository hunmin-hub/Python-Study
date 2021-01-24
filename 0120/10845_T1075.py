from collections import deque
import sys

n = int(sys.stdin.readline().strip())
qu = deque()

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    size = len(qu)
    if cmd[0] == 'push':
        qu.append(cmd[1])
    if cmd[0] == 'front':
        print(qu[0] if size else '-1')
    if cmd[0] == 'back':
        print(qu[-1] if size else '-1')
    if cmd[0] == 'size':
        print(size)
    if cmd[0] == 'empty':
        print('0' if size else '1')
    if cmd[0] == 'pop':
        print(qu.popleft() if size else '-1')