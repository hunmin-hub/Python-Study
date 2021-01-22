import sys
from collections import defaultdict

word_dict=defaultdict(lambda: defaultdict(int)) # 2차원 dict

# 사전 등록
# 앞뒤 문자가 첫번째 key / 나머지 문자들은 sort하여 두번째 key로 생성
N=int(sys.stdin.readline().rstrip())
for _ in range(0,N) :
    word=sys.stdin.readline().rstrip()
    if len(word)>1:
        first_key=word[0]+word[-1]
    else :
        first_key=word[0]
    if len(word)>2:
        second_key=''.join(sorted(word[1:-1]))
    else :
        second_key=''
    word_dict[first_key][second_key]+=1

# 해석
# 사전 등록 과정과 마찬가지로 첫번째 key와 두번째 key 를 만들어서 접근
M=int(sys.stdin.readline().rstrip())
for _ in range(0,M) :
    decode_sentence=sys.stdin.readline().rstrip().split()
    answer_list=[]
    answer=1
    for word in decode_sentence :
        if len(word)>1 :
            first_key = word[0] + word[-1]
        else :
            first_key=word[0]
        if len(word)>2 :
            second_key = ''.join(sorted(word[1:-1]))
        else :
            second_key=''
        answer_list.append(word_dict[first_key][second_key])
    for num in answer_list :
        answer*=num
    print(answer)

if N==0 and M==0 :
    print("0")