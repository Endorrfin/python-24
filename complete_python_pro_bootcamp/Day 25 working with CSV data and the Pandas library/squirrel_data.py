import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Data.csv')
grey_squirrels = data[data['Primary Fur Color'] == 'Gray']
print('GREY SQUIRRELS', grey_squirrels)

grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
print('GREY SQUIRRELS COUNT', grey_squirrels_count)

red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print('RED SQUIRRELS COUNT', red_squirrels_count)

black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print('BLACK SQUIRRELS COUNT', black_squirrels_count)

data_dict = {
    'Fur Color': ['Grey', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print('DATA DICT', data_dict)


data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('squirrel_colors_count.csv')
