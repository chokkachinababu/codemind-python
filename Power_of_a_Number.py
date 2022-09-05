import math
x,y,m=map(int,input().split())
f=math.pow(x,y)
h=int(f%m)
print(h)