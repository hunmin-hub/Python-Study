import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq = deque()

for _ in range(n):
    str = sys.stdin.readline().rstrip().split()
    if str[0] == "push":
        deq.append(int(str[1]))
    if str[0] == "pop":
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    if str[0] == "size":
        print(len(deq))
    if str[0] == "empty":
        if deq:
            print("0")
        else:
            print("1")
    if str[0] == "front":
        if deq:
            print(deq[0])
        else:
            print("-1")     
    if str[0] == "back": 
        if deq:
            print(deq[-1])
        else:
            print("-1")
