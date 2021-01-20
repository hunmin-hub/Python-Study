sentence = input()
reversed_list = []

word = ''
tag_state = 0
for letter in sentence:
    if tag_state == 1:
        
        if letter == '>':
            word += letter
            reversed_list.append(word)
            word = ''
            tag_state = 0
        else:
            word += letter
            
    elif tag_state == 0:
        
        if letter == '<':
            reversed_list.append(word[::-1])
            word = ''
            word += letter
            tag_state = 1
            
        elif letter == ' ':
            reversed_list.append(word[::-1])
            reversed_list.append(letter)
            word = ''
        else:
            word += letter
reversed_list.append(word[::-1])

answer = ''.join(reversed_list)

print(answer)