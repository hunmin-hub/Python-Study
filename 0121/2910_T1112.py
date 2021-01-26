garbage = input()

num_list = input().split()

count_num = {}

for number in num_list:
    count = num_list.count(number)
    
    if count in count_num:
        if number in  count_num[count]:
            continue
        else:
            count_num[count] += [number]
    else:
        count_num[count] = [number]

ordered_list = []
for i in sorted(count_num,reverse=True):
    for j in count_num[i]:
        ordered_list += [j] * i
        
print(' '.join(ordered_list))