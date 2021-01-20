import sys
import pprint
from collections import defaultdict

d = defaultdict(lambda : 0)
len = 0
while(1):
    s = sys.stdin.readline().strip()
    if not s:
        break
    d[s] += 1
    len += 1

sorted_dict = dict()
for i, v in sorted(d.items(), key = lambda t : t[0]):
    sorted_dict[i] = v

for i in sorted_dict:
    print(f'{i} {sorted_dict[i]/len*100: .4f}')