import sys
from collections import deque

# Input
t = int(input())

for i in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()[1:-1]
    if arr:
        arr = deque(arr.split(','))
    else:
        arr = deque()

    # 함수 수행
    err = False
    reverse = False
    for func in p:
        if func == 'R':
            reverse = not reverse
        else:
            if len(arr) > 0:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                err = True
                print('error')
                
                break
    if reverse:
        arr.reverse()
    
    # Output
    if not err:
        result = ','.join(arr)
        print(f'[{result}]')