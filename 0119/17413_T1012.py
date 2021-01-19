main_str=input()
temp=""
answer=""
open=0
for word in main_str :
    if word=='<' :
        if temp!='':
            answer+=temp[::-1]
            temp=""
        temp+=word
        open=1
    elif word=='>' :
        temp+=word
        answer+=temp
        temp=""
        open=0
    elif open==1 :
        temp+=word
    elif open==0 and word!=' ' :
        temp+=word
    elif open==0 and word==' ' :
        answer+=temp[::-1]
        answer+=' '
        temp=""

if temp!='' :
    answer+=temp[::-1]

print(answer)