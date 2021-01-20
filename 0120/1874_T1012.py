import sys
N=int(sys.stdin.readline().rstrip())
start_arr=[x for x in range(1,N+1)]
stack_arr=[]
target_arr=[]
for _ in range(N) :
    target = int(sys.stdin.readline().rstrip())
    target_arr.append(target)

answer=[]
for num in start_arr :
    if num==target_arr[0] :
        answer.append("+")
        answer.append("-")
        target_arr.pop(0)
        if len(stack_arr)==0 or len(target_arr)==0 : continue
        while stack_arr[-1]==target_arr[0] :
            answer.append("-")
            stack_arr.pop()
            target_arr.pop(0)
            if len(stack_arr)==0 or len(target_arr)==0 : break
    else :
        answer.append("+")
        stack_arr.append(num)

if len(stack_arr)!=0 :
    print("NO")
else :
    for x in answer:
        print(x)