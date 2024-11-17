a, b = list(map(int,input().split()))

while a <= b:
    if a % 2 == 0:
        print(a)

    a += 1