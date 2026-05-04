#############3.1##############
first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
operation = input("Введіть математичну дію (+, -, *, /): ")
if operation == "+":
    result = first_number + second_number
    print("Результат:", result)
elif operation == "-":
    result = first_number - second_number
    print("Результат:", result)
elif operation == "*":
    result = first_number * second_number
    print("Результат:", result)
elif operation == "/":
    if second_number == 0:
        print("Така можливість є лише у Геннадія Кернеса, якщо ви не Кернес то ділення на нуль неможливе))))")
    else:
        result = first_number / second_number
        print("Результат:", result)
else:
    print("Помилка")
#############3.2##############
def last_to_first(lst):
    if len(lst) <= 1:
        return lst
    return lst[-1:] + lst[:-1]
list1 = ['i', 'l', 'l', 'e', 'l', 'H']
list2 = [1]
list3 = []
print(f"Список 1: {last_to_first(list1)}")
print(f"Список 2: {last_to_first(list2)}")
print(f"Список 3: {last_to_first(list3)}")
#############3.3##############
def split_list(input_list):
    length = len(input_list)
    mid = (length + 1) // 2
    left_part = input_list[:mid]
    right_part = input_list[mid:]
    return [left_part], [right_part]
list1 = [1, 3, 7, 4, 6, 9]
list2 = [6, 4, 1]
list3 = []
print(f"Список 1 {list1} -> {split_list(list1)}")
print(f"Список 2 {list2} -> {split_list(list2)}")
print(f"Список 3 {list3} -> {split_list(list3)}")