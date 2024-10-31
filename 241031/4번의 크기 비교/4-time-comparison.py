a = int(input())
b = list(map(int,input().split()))

for i in b:
    if a > i:
        print(1)
    else: print(0)