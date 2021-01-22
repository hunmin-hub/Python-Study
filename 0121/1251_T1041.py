# Input
word = input()

len_word = len(word)
reversed_words = []

# 첫 번째 parsing
for i in range(1, len_word - 1):
    # 두 번째 parsing
    for j in range(i + 1, len_word):
        reversed_words.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

# 정렬
reversed_words.sort()

# Output
print(reversed_words[0])