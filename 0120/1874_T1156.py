import sys

t = int(sys.stdin.readline().strip())
temp = t
li = []
ans = []
arr = [i for i in range(1,t+1)]
while(t):
    t -= 1
    num = sys.stdin.readline().strip()
    li.append(int(num))

arr = []
j = 0
for i in range(1, temp+1):
    arr.append(i)
    ans.append('+')
    while(len(arr) != 0 and arr[-1]==li[j]):
        ans.append('-')
        j+=1
        arr.pop(-1)

if(len(arr) == 0):
    for i in ans:
        print(i)
else:
    print("NO")
