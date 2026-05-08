import random
elm = random.randint(3, 10)
lst = []
for i in range(elm):
    rand = random.randint(3, 10)
    lst.append(rand)
new_lst = [lst[0], lst[2], lst[-2]]

print(lst)
print(new_lst)
