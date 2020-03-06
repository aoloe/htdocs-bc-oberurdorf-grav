from datetime import date, timedelta

def all_fridays(year):
    d = date(year, 1, 1)
    d += timedelta(days = 4 - d.weekday())  # First Friday
    while d.year == year:
        yield d
        d += timedelta(days = 7)

for d in all_fridays(2021):
    print(f'{d.year:04}{d.month:02}{d.day:02}')
