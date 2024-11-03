a, b, c = list(map(int,input().split()))

if a > b:
    if a > c:
        print(a)
elif b > a:
    if b > c:
        print(b)
elif c > a:
    if c > b:
        print(c)