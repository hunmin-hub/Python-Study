import sys
command_number = int(sys.stdin.readline().rstrip())

que = []

for _ in range(command_number):
    command = list(sys.stdin.readline().rstrip().split())
    
    if command[0] == 'push':
        que.append(int(command[1]))
    
    elif command[0] == 'pop':
        if que:
            ele = que.pop(0)
            print(ele)
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(que))
    
    elif command[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)