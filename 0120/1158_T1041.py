from collections import deque

# Input
n, k = map(int, input().split())

answer = []
arr = deque([i for i in range(1, n + 1)])

# 요세푸스 순열
while arr:
    arr.rotate(1 - k)
    answer.append(str(arr.popleft()))
        
# Output
print(f'<{", ".join(answer)}>')