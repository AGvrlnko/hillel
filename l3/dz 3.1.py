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