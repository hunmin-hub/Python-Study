import sys
full_sentence=""
for sentence in sys.stdin:
    full_sentence+=sentence

s = full_sentence.split()

col = 0
sameline = False
for i in range(len(s)):
    if (s[i] == "<br>"):
        print()
        col = 0
    elif (s[i] == "<hr>"):
        if (col):
            print()
            print('-' * 80)
        else:
            print('-' * 80)
        col = 0
    else:
        l = len(s[i])
        if (not col):
            col = l
            print(s[i], end='')
            sameline=True
        elif(col + l + 1 <= 80):
            if sameline :
                print(' ', end='')
                col += 1
            col += l
            print(s[i], end='')
            if(col == 80):
                print()
                col = 0
                sameline = False
        else:
            print()
            col = l
            sameline = True
            print(s[i], end='')