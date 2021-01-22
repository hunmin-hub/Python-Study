# Input
n, c = map(int, input().split())
msg = map(int, input().split())

# Count numbers.
cnt_dict = {}
for num in msg:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

# Sort unique counts.
sorted_cnt_list = sorted(set(cnt_dict.values()), reverse=True)

# Output
keys_to_del = []
for cnt in sorted_cnt_list:
    for k, v in cnt_dict.items():
        if v == cnt:
            result = (str(k) + ' ') * v
            print(f'{result}', end='')
            
            keys_to_del.append(k)
    # 시간 복잡도를 줄여야 한다면 이미 출력된 숫자는 제거해주는 게 좋다.
    else:
        while keys_to_del:
            del cnt_dict[keys_to_del.pop()]