from collections import deque

a, b = map(int, input().split())

deq = deque([i for i in range(1, a + 1)])
ret = []
i = 0
while deq:
    i = (i + b - 1) % len(deq)
    ret.append(str(deq[i]))
    del deq[i]
print(f"<{', '.join(ret)}>")