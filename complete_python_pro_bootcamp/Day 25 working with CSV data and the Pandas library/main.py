# OPTION I
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)


# OPTION II
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


# OPTION III
import pandas

data = pandas.read_csv('weather_data.csv')
# print('DATA PRINT', data)
# print('DATA TYPE', type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print('TO DICT', data_dict)

# temp_list = data['temp'].to_list()
# print('TEMP LIST', temp_list)
# print('LENGTH', len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print('AVERAGE', average)

# average_easy = data['temp'].mean()
# print('AVERAGE_EASY', average_easy)

# max_temperatures = data['temp'].max()
# print('MAX_TEMPERATURES', max_temperatures)

#GET DATA IN COLUMNS
# print('DATA_CONDITION', data['condition'])
# print('DATA_CONDITION', data.condition)


#GET DATA IN ROW
# print('DATA_DAY', data[data.day == 'Monday'])
# print('MAX_TEMPERATURES_ROW', data[data.temp == data['temp'].max()])
# print('MAX_TEMPERATURES_ROW', data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


#CREATE A DATAFRAME FROM SCRATCH
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)

# data.to_csv('students_score_data.csv')











