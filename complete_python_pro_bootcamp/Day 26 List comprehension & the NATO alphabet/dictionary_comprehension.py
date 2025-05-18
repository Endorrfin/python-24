import random

# 🅰️ LIST COMPREHENSION
# new_dict = [new_key:new_value for item in list]
# new_dict = [new_key:new_value for (key, value) in dict.items()]

names = ['Nik', 'Andrew', 'Sergiy', 'Dima', 'Evgen', 'Rostislav', 'Slava', 'Yan']
students_scores = {student:random.randint(20,100) for student in names}
print('STUDENTS SCORES', students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print('PASSED STUDENTS', passed_students)



# 🅱️ CONDITIONAL DICTIONARY COMPREHENSION
# new_list = [new_item for item in list if test]

# names = ['Nik', 'Andrew', 'Sergiy', 'Dima', 'Evgen', 'Rostislav', 'Slava', 'Yan']
# short_names = [name for name in names if len(name) < 5]
# print('SHORT NAMES', short_names)
#
# long_names = [name.upper() for name in names if len(name) >= 5]
# print('LONG NAMES', long_names)

