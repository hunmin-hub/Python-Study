import sys
from collections import deque

s = sys.stdin.readline().strip()
s = s.split()
n = int(s[0])
k = int(s[1])

li = [i for i in range(1, n+1)]

j = 0
ans = []
while(len(li)):
    j += k-1
    j %= len(li)
    ans.append(li[j])
    li.pop(j)

print('<', end='')
for i in range(len(ans)):
    if(i!=len(ans)-1):
        print(str(ans[i])+', ', end="")
    else:
        print(ans[i],end='')
print('>')