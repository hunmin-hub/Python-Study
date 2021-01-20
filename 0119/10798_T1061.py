
words = [[0]*15 for i in range(5)]

for i in range(5):
    word = list(input())
    size = len(word)
    for j in range(size):
        words[i][j] = word[j]

for i in range(15):
    for j in range(5):
        if words[j][i] == 0 :
            continue
        else:
            print(words[j][i], end='')
