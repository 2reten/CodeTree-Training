age1, sex1 = input().split()
age2, sex2 = input().split()

if int(age1) >= 20 and sex1 == "M":
    print(1)
elif int(age2) >= 20 and sex2 == "M":
    print(1)
else: print(0)