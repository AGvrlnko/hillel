numbers_lst = [10, 0, 1, 5, 9, 0, 4, 3, 7]
new_lst = []
for num in numbers_lst:
    if num != 0:
        new_lst.append(num)
for num in numbers_lst:
    if num == 0:
        new_lst.append(num)
print(f'Список після переміщення: {new_lst}')
print(f'Початковий список: {numbers_lst}')