import string
import keyword
name = input("Введіть імʼя змінної: ")
dozvol_symbol = string.punctuation.replace("_", "")
result = True
if name == "":
    result = False
elif name[0].isdigit():
    result = False
elif name in keyword.kwlist:
    result = False
elif "__" in name:
    result = False
else:
    for symbol in name:
        if symbol.isupper() or symbol == " " or symbol in dozvol_symbol:
            result = False
print(result)
