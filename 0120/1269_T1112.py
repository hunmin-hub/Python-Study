number = input()
set_a = set(map(int,input().split()))
set_b = set(map(int,input().split()))

a_b = set_a - set_b
b_a = set_b - set_a 

print(len(a_b) + len(b_a))