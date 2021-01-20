# Inputs
words = []
max_len = 0
for i in range(5):
    words.append(list(input()))

    if len(words[-1]) > max_len:
        max_len = len(words[-1])

# Append
result = []
# Column
for cidx in range(max_len):
    # Row
    for ridx in range(5):
        try:
            result.append(words[ridx][cidx])
        except IndexError as err:
            pass

print(''.join(result))