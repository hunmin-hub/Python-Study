import sys
full_sentence=""
for sentence in sys.stdin:
    full_sentence+=sentence

words=full_sentence.split()
result_sentence=[]
for word in words :
    if word=='<br>' :
        result_sentence.append('\n')
    else :
        result_sentence.append(word)

current_line_len=0
hr=""
temp_list=[]
temp_line_text=""
for word in result_sentence :
    if word=='\n' :
        temp_line_text = ' '.join(temp_list)
        temp_list = []
        print(temp_line_text)
    elif word=='<hr>' :
        hr=""
        if len(temp_list)!=0 :
            temp_line_text=' '.join(temp_list)
            temp_list=[]
            print(temp_line_text)
        for _ in range(0, 80):
            hr+='-'
        print(hr)
    else :
        temp_list.append(word)
        temp_line_text=' '.join(temp_list)
        if len(temp_line_text)>80 :
            temp_list.pop(-1)
            temp_line_text = ' '.join(temp_list)
            print(temp_line_text)
            temp_list=[]
            temp_list.append(word)
temp_line_text=' '.join(temp_list)
print(temp_line_text)

