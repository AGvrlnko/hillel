def correct_sentence(text):
    first_letter = text[0]
    big_letter = first_letter.upper()
    other_text = text[1:]

    text = big_letter + other_text
    if text.endswith("."):
        return text
    else:
        return text + "."

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

