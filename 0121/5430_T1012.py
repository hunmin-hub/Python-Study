import sys
T=int(sys.stdin.readline().rstrip())

for _ in range(0,T) :
    flag=True
    r_check=0
    user_cmd=sys.stdin.readline().rstrip()
    N=int(sys.stdin.readline().rstrip())
    arr=sys.stdin.readline().rstrip()
    arr=arr.lstrip("[").rstrip("]").split(',')
    for c_cmd in user_cmd :
        if c_cmd=='R' :
            r_check+=1
        elif c_cmd=='D' :
            if len(arr)==0 or arr[0]=='' :
                flag=False
                break
            if r_check%2==0 : # 돌려도 처음상태면 leftpop
                arr.pop(0)
            else : # 반전 상태면 rightpop
                arr.pop(-1)
    if flag==False :
        print("error")
        continue
    if r_check%2==1 :
        print(f'[{",".join(arr[-1::-1])}]')
    else :
        print(f'[{",".join(arr)}]')
