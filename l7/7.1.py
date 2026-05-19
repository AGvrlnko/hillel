def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Dmytro", 31) == "Hi. My name is Dmytro and I'm 31 years old", 'Test1'
assert say_hi("Oleksandr", 26) == "Hi. My name is Oleksandr and I'm 26 years old", 'Test2'

print(say_hi("Dmytro", 31))
print(say_hi("Oleksandr", 26))
# результат функції вивів чисто для себе, щоб бачити
print('ОК')