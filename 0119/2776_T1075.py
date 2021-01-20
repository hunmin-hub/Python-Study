t = int(input())


for _ in range(t):
    n = int(input())
    n_list = (set(input().split()))
    m = int(input())
    m_list = input().split()
    for m in m_list:
        if m in n_list:
            print(1)
        else:
            print(0)


