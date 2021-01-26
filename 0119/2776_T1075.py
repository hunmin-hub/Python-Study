import sys

t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = set(sys.stdin.readline().strip().split())
    m = int(input())
    arr2 = sys.stdin.readline().strip().split()

    ret = ['1' if x in arr1 else '0' for x in arr2]
    print("\n".join(ret))
