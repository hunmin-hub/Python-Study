import sys

# Input
n, m = map(int, input().split())

# 도감
book_num = {}
book_name = {}
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    
    book_num[i] = name
    book_name[name] = i

# Output 
for _ in range(m):
    x = sys.stdin.readline().strip()
    
    if x.isalpha():
        print(book_name[x])
    else:
        print(book_num[int(x)])