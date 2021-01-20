import sys
from collections import defaultdict
s = sys.stdin.readline().strip()
s = s.split()
n = int(s[0])
m = int(s[1])
li1 = defaultdict(lambda : 0)
li2 = defaultdict(lambda : '0')
for i in range(1,n+1):
    temp = sys.stdin.readline().strip()
    li1[temp] = i
    li2[i] = temp

for i in range(m):
    temp = sys.stdin.readline().strip()
    if(temp.isdigit()):
        print(li2[int(temp)])
    else:
        print(li1[temp])
