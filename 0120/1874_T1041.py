import sys
            
# Input
n = int(input())
seq = [int(sys.stdin.readline().strip()) for i in range(n)]
seq.reverse()

stack = []
answer = []

def pop():
    while stack and seq:
        if stack[-1] == seq[-1]:
            stack.pop()
            answer.append('-')

            seq.pop()
        else:
            break

# Append and pop.
for i in range(1, n + 1):
    pop()

    stack.append(i)
    answer.append('+')
else:
    pop()

# Output
if len(seq) == 0:
    [print(i) for i in answer]
else:
    print('NO')