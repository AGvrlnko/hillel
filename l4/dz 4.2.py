#################4.2################
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
result = 0
if len(num_lst) == 0:
    result = 0
else:
    for i in range (len(num_lst)):
        if i % 2 == 0:
         suma = suma + num_lst[i]
        result = suma * num_lst [-1]
print(result)