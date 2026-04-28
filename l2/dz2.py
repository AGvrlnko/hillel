##########################################################################################
import math
user_input = input("Введіть число:")
number = int(user_input)
square = number ** 2
print(f"Квадрат числа: {square}")
##########################################################################################
num1 = float(input("Введіть число №1: "))
num2 = float(input("Введіть число №2: "))
num3 = float(input("Введіть число №3: "))
avarage = (num1 + num2 + num3) / 3
print(f"Середнє арифметичне: {avarage}")
##########################################################################################
tot_minutes = int(input("Введіть кількість хвилин: "))
hours = tot_minutes // 60
minutes = tot_minutes % 60
print(f"Годин {hours} та хвилин {minutes}")
##########################################################################################
price = float(input("Введіть ціну: "))
discount = float(input("Введіть розмір знижки в %: "))
discount_amount = price * (discount / 100)
final_price = price - discount_amount
print(f"Кінцева ціна: {final_price}")
##########################################################################################
number = int(input("Введіть число: "))
last_digit = number % 10
print(f"Остання цифра: {last_digit}")
##########################################################################################
leght = float(input("Введіть довжину: "))
widht = float(input("Введіть ширину: "))
perimetr = 2 * (leght + widht)
print(f"Периметр: {perimetr}")
##########################################################################################
number = int(input("Введіть чотирьохзначне число: "))
digit1, zalyshok = divmod(number, 1000)
digit2, zalyshok = divmod(zalyshok, 100)
digit3, digit4 = divmod(zalyshok, 10)
print(digit1)
print(digit2)
print(digit3)
print(digit4)