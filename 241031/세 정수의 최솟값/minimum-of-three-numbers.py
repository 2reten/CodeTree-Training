a = list(map(int,input().split()))
mn = a[0]+1
for i in a:
    if i < mn:
        mn = i
print(mn)