test_count = int(input())

for i in range(test_count):
    _ = input()
    memo_1 = set(list(input().split()))

    _ = input()
    memo_2 = list(input().split())

    for ele in memo_2:
        if ele in memo_1:
            print(1)
        else:
            print(0)