import sys
import math
input=sys.stdin.readline
def func_value(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy,t) :
    first=((Cx-Ax)+((Dx-Cx)-(Bx-Ax))*t)*((Cx-Ax)+((Dx-Cx)-(Bx-Ax))*t)
    second=((Cy-Ay)+((Dy-Cy)-(By-Ay))*t)*((Cy-Ay)+((Dy-Cy)-(By-Ay))*t)
    return first+second

def gradient_value(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy,t) :
    first=2*(Cx-Ax)*((Dx-Cx)-(Bx-Ax))+2*((Dx-Cx)-(Bx-Ax))*((Dx-Cx)-(Bx-Ax))*t
    second=2*(Cy-Ay)*((Dy-Cy)-(By-Ay))+2*((Dy-Cy)-(Dy-Ay))*((Dy-Cy)-(By-Ay))*t
    return first+second

Ax,Ay,Bx,By,Cx,Cy,Dx,Dy=map(float,input().rstrip().split(' '))
val=0
answer=min(func_value(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, 0),func_value(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, 1))
while val<1 :
    val+=0.000001
    answer = min(answer, func_value(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, val))

print(f'{math.sqrt(answer):.10f}')