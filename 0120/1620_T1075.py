import sys

n, m = map(int, sys.stdin.readline().strip().split())

dic1 = {}
dic2 = {}

for i in range(1, n+1):
    word = sys.stdin.readline().strip()
    dic1[str(i)] = word
    dic2[word] = str(i)

for _ in range(m):
    word = sys.stdin.readline().strip()
    if word.isdigit():
        print(dic1[word])
    else:
        print(dic2[word])