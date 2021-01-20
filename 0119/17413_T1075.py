s = input()
flag = 0
list = []
word = []
reverse = []

for c in s:
    if flag:
        word.append(c)
        if (c == '>'):
            flag = 0
            list.append("".join(word))
            word.clear()
    else:
        if c == '<':
            flag = 1
            word.append(c)
            list.append("".join(reverse)[::-1])
            reverse.clear()
        elif c == ' ':
            list.append("".join(reverse)[::-1])
            list.append(" ")
            reverse.clear()

        else:
            reverse.append(c)
list.append("".join(reverse)[::-1])
print("".join(list))