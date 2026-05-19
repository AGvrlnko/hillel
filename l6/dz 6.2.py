number = int(input("Введіть кількість секунд: "))
seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60

days = number // seconds_in_day
numbers = number % seconds_in_day

hours = numbers // seconds_in_hour
numbers = numbers % seconds_in_hour

minutes = numbers // seconds_in_minute
seconds = number % seconds_in_minute

if 11 <= days % 100 <= 14:
    word = "Днів"
elif days % 10 == 1:
    word = "День"
elif 2 <= days % 10 <= 4:
    word = "Дні"
else:
    word = "Днів"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)
print(days, word + ",", hours + ":" + minutes + ":" + seconds)
