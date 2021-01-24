from collections import deque
import sys

n = int(sys.stdin.readline().strip())
st = deque()
idx = 1
ret = []

for _ in range(n):
    m = int(sys.stdin.readline().strip())

    while idx <= m:
        st.append(idx)
        ret.append('+')
        idx += 1

    if st[-1] == m:
        st.pop()
        ret.append('-')
    else:
        print("NO")
        break
else:
    print("\n".join(ret))
