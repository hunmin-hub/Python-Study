import sys

t = int(sys.stdin.readline().strip())
while(t):
    t -= 1
    command = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    li = sys.stdin.readline().strip()[1:-1].split(',')
    err = False
    dir = True
    for i in command:
        if(i=='R'):
            dir = not dir
        if(i=='D'):
            if(n):
                if(dir):
                    li.pop(0)
                    n -= 1
                else:
                    li.pop(-1)
                    n -= 1
            else:
                print("error")
                err = True
                break
    if(not dir):
        li = li[::-1]
    if(not err):
        print('[',end='')
        for i in range(len(li)):
            if(i != len(li)-1):
                print(str(li[i])+',', end='')
            else:
                print(str(li[i]), end='')
        print(']')