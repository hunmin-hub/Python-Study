A=input()
target=input()
target_length=len(target)
answer=0
while True :
    idx=A.find(target)
    if idx==-1 : break
    A=A[idx+target_length:]
    answer+=1

print(answer)