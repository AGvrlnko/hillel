number = int(input("Введіть ціле число: "))
while number > 9:
    result = 1
    for digit in str(number):
        result = result * int(digit)
    number = result
print(number)