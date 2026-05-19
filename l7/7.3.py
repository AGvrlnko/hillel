def second_index(text, some_str):
  first_position = text.find(some_str)

  if first_position == -1:
      return None
  second_position = text.rfind(some_str, first_position + 1)
  if second_position == -1:
      return None
  else:
    return second_position

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

