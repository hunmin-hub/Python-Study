import sys
from collections import defaultdict

def word_split(i, j, s):
    a = s[0:i]
    b = s[i:j]
    c = s[j:]

    a = a[::-1]
    b = b[::-1]
    c = c[::-1]
    d = a+b+c
    s = ''
    for i in d:
        s = s+i
    return s

d = defaultdict(lambda : 0)

s = sys.stdin.readline().strip()
li = []
for i in range(1,len(s)-1):
    for j in range(i+1, len(s)):
        li.append(word_split(i,j,s))

li.sort()
print(li[0])
