b, a = list(map(int,input().split()))

while b >= a:
    if b % 2 == 0:
        print(b)
    b -= 1
