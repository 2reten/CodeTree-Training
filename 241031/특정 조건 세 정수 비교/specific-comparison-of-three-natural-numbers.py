a, b, c = list(map(int,input().split()))

if a<=b:
    if a<=c:
        min = a
    else:
        min = c
else:
    if b<=c:
        min =b
    else:
        min = c


if a == min :
    print(int(a==min), end=" ")
else: print(0, end=' ')
    
if a==b and b==c:
    print(int( a==b and b==c))
else: print(0)