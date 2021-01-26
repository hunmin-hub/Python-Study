# Input
s = input()

k_list = [1]
# 실제로 문자열을 계산하지 않고 문자열의 길이만 계산함.
q_len_list = [0]

# Decoding
for i, c in enumerate(s):
    if c == '(':
        # 새로운 K 추가
        k_list.append(int(s[i - 1]))
        # Q 업데이트
        q_len_list[-1] -= 1 
        # 새로운 Q 추가
        q_len_list.append(0)
    elif c == ')':
        # 마지막 Q와 K 꺼내서 부분 문자열 만든 후
        sub_str = q_len_list.pop() * k_list.pop()
        # 이전 Q 뒤에 붙임.
        q_len_list[-1] += sub_str
    else:
        q_len_list[-1] += 1
        
# Output
print(q_len_list[0])


"""압축을 모두 푼 문자열을 구해서 푸는 방법 (메모리 초과로 인해 통과 안 됨)"""
# Input
s = input()

k_list = [1]
# q_list = ['']

# Decoding
for i, c in enumerate(s):
    if c == '(':
        # 새로운 K 추가
        k_list.append(int(q_list[-1][-1]))
        # Q 업데이트
        q_list[-1] = q_list[-1][:-1]
        # 새로운 Q 추가
        q_list.append('')
    elif c == ')':
        # 마지막 Q와 K 꺼내서 부분 문자열 만든 후
        sub_str = q_list.pop() * k_list.pop()
        # 이전 Q 뒤에 붙임.
        q_list[-1] += sub_str
    else:
        q_list[-1] += c
        
# Output
print(len(q_list[0]))