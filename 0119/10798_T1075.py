list = []
max_len = 0
for _ in range(5):
    word = input()
    list.append(word)
    max_len = max(max_len, len(word))

ret = []
"""
for i in range(max_len):
    for j in range(5):
        if i < len(list[j]):
            ret.append(list[j][i])
"""
ret = [list[j][i] for i in range(max_len) for j in range(5) if i < len(list[j])]
print("".join(ret))