import pandas

student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print('KEY:', key, 'VALUE:', value)

student_data_frame = pandas.DataFrame(student_dict)
# print('STUDENT DATA FRAME', student_data_frame)


# Loop through rows of a data frame:
# for (key, value) in student_data_frame.items():
#     print('KEY:', key, 'VALUE:', value)

# Loop through a data frame:
for (index, row) in student_data_frame.iterrows():
    # print('INDEX:', index, 'ROW:', row)
    # print('ROW:', row.student)
    if row.student == 'Angela':
        print(row.score)