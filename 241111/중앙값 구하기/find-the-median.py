lst = input().split()
lst = list(map(int, lst))  

sort_list = []

max_score = 0

for i in lst:
    if int(i) >= max_score:
        max_score = i

sort_list.append(max_score)
lst.remove(max_score)

max_score = 0

for i in lst:
    if i >= max_score:
        max_score = i

sort_list.append(max_score)
print(sort_list[-1])