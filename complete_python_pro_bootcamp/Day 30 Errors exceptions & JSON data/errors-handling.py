
# FILE NOT FOUND
# with open(a_file.txt) as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")


# KEY ERROR
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']


# INDEX ERROR
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]


# TYPE ERROR
# text = 'abc'
# print(text + 5)


# BMI EXAMPLE
height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human Height should not be over 3 meters.')

bmi = weight / height ** 2
print(bmi)