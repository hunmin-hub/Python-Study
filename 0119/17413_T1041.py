# Inputs
input_str = input()

word = []
tag = []
b_tag = False

for c in input_str:
    # 태그
    if b_tag:
        tag.append(c)

        # 태그 끝
        if c == '>':
            b_tag = False

            # 태그인 경우
            if len(tag) >= 3:
                print(''.join(tag), end='')
            # 길이가 짧아서 태그가 아닌 경우
            else:
                print(''.join(tag)[::-1], end='')
            tag = []
    # 단어
    else:
        # 태그 시작
        if c == '<':
            print(''.join(word)[::-1], end='')
            word = []

            tag.append(c)

            b_tag = True
        # 공백 문자
        elif c == ' ':
            print(''.join(word)[::-1] + ' ', end='')
            word = []
        else:
            word.append(c)
# 마지막 단어 출력
else:
    if word:
        print(''.join(word)[::-1], end='')