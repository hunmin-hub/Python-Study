import sys
T = int(input())
for i in range(T):
    N = int(input())
    note1 = sys.stdin.readline().rsplit()

    dic = {}
    for v in note1:
        dic[v] = 1
    M = int(input())
    note2 = sys.stdin.readline().rsplit()

    for v in note2:
        if v in dic:
            print(1)
        else:
            print(0)


