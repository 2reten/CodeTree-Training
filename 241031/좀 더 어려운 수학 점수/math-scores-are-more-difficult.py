math1, eng1 = list(map(int,input().split()))
math2, eng2 = list(map(int,input().split()))

if math1 > math2:
    print("A")
elif math1 == math2:
    if eng1 > eng2:
        print("A")
    else: print("B")
else: print("B")