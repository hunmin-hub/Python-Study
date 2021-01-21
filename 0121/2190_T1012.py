from collections import Counter

N,C=map(int,input().split())
arr=list(input().split())

count_arr=dict(Counter(arr)) # 단순한 Counter 함수로는 먼저 나온 수들의 빈도수를 알려주지, sort 를 시켜주진 않는다.
count_arr=dict(sorted(count_arr.items(), key=lambda x: x[1], reverse=True)) # 내림차순

answer_list=[]
for k,v in count_arr.items() :
    for _ in range(0,v) :
        answer_list.append(k)

print(' '.join(answer_list))
