a, b = list(map(int,input().split()))

if a >= 90:
    if b >= 95:
        print(100000)
    elif 95 > b >= 90:
        print(50000)
    else: print(0)
else: print(0)