import string
text = input("Введіть рядок: ")
clean_text = ""
for symbol in text:
    if symbol not in string.punctuation:
        clean_text += symbol
words = clean_text.split()
tag = "#"
for word in words:
    tag += word.capitalize()
if len(tag) > 140:
    tag = tag[:140]
print(tag)