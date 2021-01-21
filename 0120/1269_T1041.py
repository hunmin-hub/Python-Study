# Input
n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

"""
풀이 1. set.symmetric_difference() 사용
"""
# 대칭차집합
print(len(a ^ b))

"""
풀이 2. Raw code
"""
# a_diff_b = [i for i in a if i not in b]
# b_diff_a = [i for i in b if i not in a]

# print(len(a_diff_b) + len(b_diff_a))