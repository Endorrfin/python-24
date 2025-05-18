

numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
    print(add_1)
    print(new_list)

# 🅰️ LIST COMPREHENSION
# new_list = [new_item for item in list]

array = [1, 2, 3, 4, 5]
new_comprehension_list = [item + 1 for item in array]
print('INITIAL ARRAY', array)
print('COMPREHENSION LIST', new_comprehension_list)

name = 'Leonid'
new_name = [letter.upper() for letter in name]
print('NEW NAME', new_name)


range_list = [number * 10 for number in range(1,5)]
print('RANGE LIST', range_list)


# 🅱️ CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in list if test]

names = ['Nik', 'Andrew', 'Sergiy', 'Dima', 'Evgen', 'Rostislav', 'Slava', 'Yan']
short_names = [name for name in names if len(name) < 5]
print('SHORT NAMES', short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print('LONG NAMES', long_names)

