

def reversePrint(f_word):

    for i in range(len(f_word)-1, -1, -1):
        print(f_word[i], end='')

    f_word.clear()


def tagPrint(f_word):
    for i in range(len(f_word)):
        print(f_word[i], end='')
    print(end='>')
    f_word.clear()


words = input()
tag_flag = False
word = []
tagWord = []
for ch in words:

    if (not tag_flag) and ch == ' ':
        reversePrint(word)
        print(end=' ')
        continue
    elif ch == '<':
        reversePrint(word)
        tag_flag = True

    elif ch == '>':
        tagPrint(tagWord)
        tag_flag = False
        continue

    if tag_flag:
        tagWord.append(ch)
    else:
        word.append(ch)

reversePrint(word)

