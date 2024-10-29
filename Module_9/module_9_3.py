

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = ((len(x) - len (y)) for x, y  in zip(first,  second) if len(x) != len(y))

second_result = map(lambda x, y: len(x) == len(y), first, second)

print(list(first_result))
print(list(second_result))

# second_result = ((len(x) == len(y)) for x in first for y in second if y == range(0,len(x)))
# print(list(second_result))
#
# second_result = (y  for y in second if len(y) in range(0,24))
# print(list(second_result))

