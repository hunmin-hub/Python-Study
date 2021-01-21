import sys
poket_n, pro_n = list(map(int, sys.stdin.readline().rstrip().split()))

n_to_po = {}
po_to_n = {}

for number in range(1, poket_n + 1):
    poketmon = sys.stdin.readline().rstrip()
    
    n_to_po[number] = poketmon
    po_to_n[poketmon] = number
    

for _ in range(pro_n):
    problem = sys.stdin.readline().rstrip()
    
    if problem.isdigit():
        print(n_to_po[int(problem)])
    else:
        print(po_to_n[problem])