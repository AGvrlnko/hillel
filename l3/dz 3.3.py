###############3.3##############
lst = [1,2,3,4,5,6,7,8,9,10]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []
zriz = (len(lst) + 1) // 2
result = [lst[:zriz],lst[zriz:]]
print(result)