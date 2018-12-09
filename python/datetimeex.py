import datetime

date = datetime.date(2017, 7, 12)
print(date)

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday - tdelta)

bday = datetime.date(2019, 7, 21)

till_bday = bday - tday
print(till_bday.days)

my_bday = tday + datetime.timedelta(days=224)
print(my_bday)