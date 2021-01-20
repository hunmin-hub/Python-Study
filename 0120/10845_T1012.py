import sys
N=int(sys.stdin.readline().rstrip())
v_queue=[]
for _ in range(N) :
    A=list(sys.stdin.readline().rstrip().split(" "))
    if A[0]=="push" :
        v_queue.append(int(A[1]))
    elif A[0]=="front" :
        if len(v_queue)==0 :
            print("-1")
            continue
        print(v_queue[0])
    elif A[0]=="back" :
        if len(v_queue)==0 :
            print("-1")
            continue
        print(v_queue[-1])
    elif A[0]=="size" :
        print(len(v_queue))
    elif A[0]=="pop" :
        if len(v_queue)==0 :
            print("-1")
            continue
        print(v_queue.pop(0))
    elif A[0]=="empty" :
        if len(v_queue)==0 :
            print("1")
        else :
            print("0")
