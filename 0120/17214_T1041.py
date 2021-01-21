def convert_coeff2str(coeff: int) -> str:
    if coeff == 1:
        return '+'
    elif coeff == -1:
        return '-'
    else:
        return f'{coeff:+}'

# Input
expression = input()

# 일차항의 계수가 1일 경우
if expression.startswith('x'):
    expression = '1' + expression
    
# 각 항의 계수 분리
coeff_list = [i for i in expression.split('x') if i]

# 적분
# 항이 한 개인 경우
if len(coeff_list) == 1:
    coeff = int(coeff_list[0])
    
    # 일차항만 있는 경우
    if 'x' in expression:
        answer = f'{convert_coeff2str(coeff // 2)}xx+W'
    # 상수항만 있는 경우
    else:
        if coeff == 0:
            answer = 'W'
        else:
            answer = f'{convert_coeff2str(coeff)}x+W'
# 항이 두 개인 경우
else:
    coeff1, coeff2 = map(int, coeff_list)
    answer = f'{convert_coeff2str(coeff1 // 2)}xx{convert_coeff2str(coeff2)}x+W'

# 맨 앞 '+' 제거
if answer.startswith('+'):
    answer = answer[1:]
    
# Output
print(answer)