import sys

str = sys.stdin.readline().rstrip()

ans =''
tag = ''
temp = ''
check = False
for i in range(len(str)):
    if(str[i] == '<' or check):
        check = True
        temp = temp[::-1]
        ans = ans + temp
        temp = ''
        tag = tag + str[i]
        if(str[i]=='>'):
            check = False
    elif(str[i] == ' '):
        ans = ans + temp[::-1]+' '
        temp = ''
    else:
        ans = ans + tag
        tag = ''
        temp = temp + str[i]

ans = ans+temp[::-1]
ans = ans+tag
print(ans)

