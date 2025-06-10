import datetime as dt

now = dt.datetime.now()
print('NOW', now)
print(type(now))

year = now.year
print('YEAR', year)
print(type(year))

month = now.month
print('MONTH', month)

day_of_week = now.weekday()
print('DAY OF WEEK', day_of_week)

date_of_birth = dt.datetime(year= 1992, month= 10, day= 17, hour=4)
print('DATE OF BIRTH', date_of_birth)