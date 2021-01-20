# Inputs
n_test_case = int(input())

for i in range(n_test_case):
    n_num1 = int(input())
    note1 = frozenset(input().split())
    n_num2 = int(input())
    note2 = input().split()

    # 수첩2의 숫자가 수첩1에 있으면 출력
    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)