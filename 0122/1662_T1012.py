from collections import deque
import sys
stack_decoder=deque()
encode_sentence=sys.stdin.readline().rstrip()

# 문자열 그대로 deque에 push하면 메모리초과가 나므로, 길이로 변환해서 넣어준다.
# 어짜피 구하는것은 최종 길이이기 때문.
def get_KQ() :
    len_Q=0
    while True :
        if stack_decoder[-1]=='(' :
            stack_decoder.pop()
            get_k=int(stack_decoder.pop())
            KQ=(get_k, len_Q)
            return KQ
        else :
            temp=stack_decoder.pop()
            if type(temp)==str :
                len_Q+=1
            else :
                len_Q+=temp

for word in encode_sentence :
    if word==')' :
        ## K(Q) 에서 K값, Q값(길이) 추출
        K,Q=get_KQ()
        stack_decoder.append(K*Q)
    else :
        stack_decoder.append(word)

answer=0
for x in stack_decoder :
    if type(x)==str :
        answer+=1
    else :
        answer+=x

print(answer)