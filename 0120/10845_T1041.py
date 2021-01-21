import sys
from collections import deque

# Input
n_cmd = int(input())

# Que
que = deque()

# 명령 처리 및 Output
for i in range(n_cmd):
    cmd = sys.stdin.readline().strip()
    
    # Push
    if cmd.startswith('pu'):
        que.append(int(cmd.split()[1]))
    # Pop
    elif cmd.startswith('p'):
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    # Size
    elif cmd.startswith('s'):
        print(len(que))
    # Empty
    elif cmd.startswith('e'):
        if len(que) == 0:
            print(1)
        else:
            print(0)
    # Front
    elif cmd.startswith('f'):
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    # Back
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])