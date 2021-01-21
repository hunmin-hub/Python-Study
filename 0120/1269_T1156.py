import sys

s = sys.stdin.readline().strip()

A = set()
B = set()
a = sys.stdin.readline().strip()
a = a.split()
for i in a:
    A.add(i)

b = sys.stdin.readline().strip()
b = b.split()
for i in b:
    B.add(i)

C = A-B
D = B-A

E = len(C) + len(D)
print(E)