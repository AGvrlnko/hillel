def add_one(some_list):
    number_text = ""
    for digit in some_list:
        number_text = number_text + str(digit)
    number = int(number_text)
    number = number + 1
    result = []
    for digit in str(number):
        result.append(int(digit))
    return result
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
print("Test1 пройдено")
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
print("Test2 пройдено")
assert add_one([0]) == [1], 'Test3'
print("Test3 пройдено")
assert add_one([9]) == [1, 0], 'Test4'
print("Test4 пройдено")
print("Усі тести пройдено")