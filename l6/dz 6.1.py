import string
letters = string.ascii_letters
text = input("Введіть дві літери через дефіс: ")
first_letter = text[0]
second_letter = text[2]
result = ""
can_add = False
for letter in letters:
    if letter == first_letter:
        can_add = True
    if can_add == True:
        result = result + letter
    if letter == second_letter:
        can_add = False
print(result)