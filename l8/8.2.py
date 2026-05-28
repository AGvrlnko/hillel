def is_palindrome(text):
    clean_text = ""
    for symbol in text:
        if symbol.isalnum():
            clean_text = clean_text + symbol.lower()
    return clean_text == clean_text[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('OP') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("Перевірено")