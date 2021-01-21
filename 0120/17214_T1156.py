import sys

s = sys.stdin.readline().strip()

def integral(a, b):
    if(a==0):
        return ""
    temp = ""
    if(a//(b+1) != 1):
        temp = temp + str(a//(b+1))
    for i in range(b+1):
        temp = temp + 'x'
    return temp

a = 0
b = 0
ans = ''
for i in s:
    if(i.isdigit()):
        a = 10*a + int(i)
    elif(i == 'x'):
        b += 1
    elif(i == '+' or i == '-'):
        temp = integral(a,b)
        ans = ans + temp + i
        a = 0
        b = 0
temp = integral(a,b)
if(not temp):
    ans = ans + "W"
else :
    ans = ans + temp + "+" + "W"
print(ans)
