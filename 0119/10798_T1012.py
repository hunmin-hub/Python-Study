board=list()
for _ in range(0,5) :
    A=list(input())
    N=len(A)
    for t_blank in range(15-N) :
        A.append('')
    board.append(A)
temp=""
for i in range(0,15) :
    for j in range(0,5) :
        if board[j][i]!='' :
            temp+=board[j][i]
print(temp)