import sys
word=sys.stdin.readline().rstrip()
N=len(word)
answer_list=[]
temp=""
for i in range(0,N-2) :
    for j in range(i+1,N-1) :
        #print(f'{0}부터{i}까지, {i+1}부터{j}까지, {j+1}부터{N-1}까지')
        temp+=word[i::-1]
        temp+=word[j:i:-1]
        temp+=word[N-1:j:-1]
        answer_list.append(temp)
        temp = ""

answer_list.sort()
print(answer_list[0])