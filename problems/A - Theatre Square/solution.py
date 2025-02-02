import math
m,n,a = map(int,input().split())

width = 0
height = a
ans = 0

width = math.ceil(m/a)
height = math.ceil(n/a)
ans = width*height
print(ans)