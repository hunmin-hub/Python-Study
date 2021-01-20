import sys
input=sys.stdin.readline

N, M=list(input().split(' '))
N=int(N)
M=int(M)
poket_book={}
for idx in range(N) :
    poket_name=input().rstrip()
    if poket_name not in poket_book :
        poket_book[poket_name]=idx+1

poket_num=list(poket_book.keys())

for _ in range(M) :
    target=input().rstrip()
    if target.isdigit() :
        print(poket_num[int(target)-1])
    else :
        print(poket_book[target])