import sys
times = int(sys.stdin.readline().rstrip())


for _ in range(times):
    
    func = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline().rstrip())
    num_list = sys.stdin.readline().rstrip()

  
    num_list = num_list[1:-1].split(',')
    
    count_R = 0
    
   
    
    if func.count('D') > length:
        print('error')
        
    else:
        for process in func:
            if process == 'R':
                count_R += 1

            else:
                if count_R % 2 == 0:
                    num_list.pop(0)


                else:
                    num_list.pop(-1)

        if count_R % 2 == 1:
            print(f'[{",".join(num_list[::-1])}]')
        else:
            print(f'[{",".join(num_list)}]')