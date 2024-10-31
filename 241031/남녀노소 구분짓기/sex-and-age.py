sex = int(input())
age = int(input())

if sex == 0 and age >=19:
    print("MAN")
elif sex == 0 and age < 19:
    print("BOY")
if sex != 0 and age >=19:
    print("WOMAN")
elif sex != 0 and age < 19:
    print("GIRL")