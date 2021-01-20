from collections import deque

josephus = deque()
N, K =map(int,input().split(" "))

for i in range(1,N+1) :
    josephus.append(i)

answer=[]
while len(josephus)>0 :
    josephus.rotate(1-K)
    answer.append(str(josephus.popleft()))

temp=', '.join(answer)
print(f'<{temp}>')
