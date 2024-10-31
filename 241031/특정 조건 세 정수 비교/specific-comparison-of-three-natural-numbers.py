a, b, c = list(map(int,input().split()))

if a == b or a == c:
    print(1, end=' ')
elif a == b == c:
    print(1,1)
else : print(0,0)