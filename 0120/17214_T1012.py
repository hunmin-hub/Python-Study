temp = input()
poly=[]
if temp.count('x')==0 :
    level=1
    poly.append(temp)
else :
    level=2
    if temp.count('x+') :
        poly=temp.split('x+')
    elif temp.count('x-') :
        poly=temp.split('x')
    else :
        poly.append(temp[:-1])
answer_list=[]
for cf in poly :
    answer=""
    temp=int(cf)//level
    if temp==0 :
        level-=1
        continue
    if temp==-1 :
        answer+='-'
    elif temp!=1 :
        answer+=str(temp)
    if level==2 :
        answer+='xx'
    else :
            answer+='x'
    level-=1
    answer_list.append(answer)

if len(answer_list)==0 :
    print("W")
elif len(answer_list)==1 :
    print(f"{'+'.join(answer_list)}+W")
else :
    if answer_list[1].count('-') :
        print(f"{''.join(answer_list)}+W")
    else :
        print(f"{'+'.join(answer_list)}+W")