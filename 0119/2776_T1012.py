T=int(input())
for TC in range(0,T) :
    dic={}
    N=int(input())
    A_num=input().split(' ')
    for num in A_num :
        if num in dic :
            dic[num]+=1
        else :
            dic[num]=1
    M=int(input())
    B_num=input().split(' ')
    for num in B_num :
        if num in dic :
            print(1)
        else :
            print(0)