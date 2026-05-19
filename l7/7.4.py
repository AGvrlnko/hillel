
def common_elements():
    list_3 = [number for number in range(100) if number % 3 == 0]
    list_5 = [number for number in range(100) if number % 5 == 0]
    set_3 = set(list_3)
    set_5 = set(list_5)
    result = set_3.intersection(set_5)
    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print (common_elements())