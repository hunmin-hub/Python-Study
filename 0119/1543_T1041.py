# Inputs
doc = input()
word = input()

# Count
print(doc.count(word))

"""
뭐 한 거지...
"""
# len_word = len(word)

# idx = 0
# cnt = 0

# while True:
#     # 앞에서부터 부분 문자열 검색
#     found_idx = doc.find(word, idx)
    
#     # 더 이상 없을 경우
#     if found_idx == -1:
#         break
#     # 있을 경우
#     else:
#         cnt += 1

#         # Index 업데이트
#         idx += found_idx + len_word

# print(cnt)
