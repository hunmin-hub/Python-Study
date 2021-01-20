from collections import deque
import sys

dq = deque()
n = int(input())
while(n):
    n -= 1
    s = sys.stdin.readline().strip()
    s = s.split()
    if (len(s) == 2):
        dq.append(int(s[1]))
    elif (s[0] == 'front'):
        if(len(dq) != 0):
            print(dq[0])
        else:
            print(-1)
    elif (s[0] == 'size'):
        print(len(dq))
    elif (s=='empty'):
        if(len(dq) == 0):
            print(1)
        else:
            print(0)
    elif(s[0] == 'back'):
        if(len(dq) == 0):
            print(-1)
        else:
            print(dq[-1])
    elif(s[0] =='pop'):
        if(len(dq)==0):
            print(-1)
        else:
            print(dq.popleft())
    elif(s[0] == 'empty'):
        if(len(dq)==0):
            print(1)
        else:
            print(0)