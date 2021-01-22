import sys
from collections import defaultdict
from collections import OrderedDict

s = sys.stdin.readline().strip()

d = defaultdict(lambda : 0)
num = sys.stdin.readline().strip().split()
for i in num:
    d[int(i)] += 1

sorted_list = sorted(d.items(), key = lambda t : t[1], reverse=True)
li = ''
for k,v in sorted_list:
    for i in range(v):
        li = li + str(k) + ' '
li.strip()
print(li)