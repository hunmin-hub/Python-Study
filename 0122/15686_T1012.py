import sys
INF=99999999
global mini_distance
mini_distance=INF
N,M=map(int,sys.stdin.readline().rstrip().split(' '))
choice_chicken=[]
house_location=[]
chicken_location=[]
city_map=[]
for _ in range(0,N) :
    line_map=sys.stdin.readline().rstrip().split(' ')
    city_map.append(line_map)

for i, line_map in enumerate(city_map) :
    for j, data in enumerate(line_map) :
        if data=='1' : # 집이면
            house_location.append((i,j))
        elif data=='2' : # 치킨집이면
            chicken_location.append((i,j))
            choice_chicken.append(False)

def distance_calc(h_x,h_y,c_x,c_y) : # 집 좌표와 치킨 집 좌표
    return abs(h_x-c_x)+abs(h_y-c_y)

def DFS(vertex, picked, count):
    choice_chicken[vertex]=picked
    if vertex == len(chicken_location)-1 :
        if count==M :
            current_answer=0
            for house in house_location :
                min_distance=INF
                for i in range(0,len(chicken_location)) :
                    if choice_chicken[i] :
                        h_x, h_y=map(int,house)
                        c_x, c_y=map(int,chicken_location[i])
                        temp=distance_calc(h_x,h_y,c_x,c_y)
                        if min_distance>temp :
                            min_distance=temp
                current_answer+=min_distance
            global mini_distance
            if mini_distance>current_answer :
                mini_distance=current_answer
        return

    DFS(vertex + 1, True, count + 1)
    DFS(vertex + 1, False, count)

DFS(-1,False,0)
print(mini_distance)