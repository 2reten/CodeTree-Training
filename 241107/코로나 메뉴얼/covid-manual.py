hu1 = input().split())
hu2 = input().split())
hu3 = input().split())
hu = [hu1, hu2, hu3]
a =0
b = 0
c = 0
d = 0
for i in hu:
    if i[0]=="Y" and i[1]>=37:
        a += 1
    elif i[0]=="N" and i[1]>=37:
        b += 1
    elif i[0]=="Y" and i[1] < 37:
        c += 1
    else:d+=1
if a >= 2:
    print("E")
else: print("N")