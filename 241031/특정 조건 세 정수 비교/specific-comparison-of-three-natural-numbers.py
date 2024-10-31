a, b, c = list(map(int,input().split()))

if a == b == c:
    print(1, 1)
elif a == b or a == c:
    print(1, 0)
else : print(0,0)