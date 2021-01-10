import calendar
yy = 1985
mm = 9
print(calendar.weekheader(1))

print(calendar.firstweekday())

print(calendar.month(2020, 4))
print(calendar.monthcalendar(2020, 4))

print(calendar.calendar(1918))
print(calendar.calendar(2020))
print(calendar.calendar(2019))
day_of_the_week = calendar.weekday(2050, 4, 10)
print(day_of_the_week)
is_leap = calendar.isleap(2100)
print(is_leap)

how_many_leap_days = calendar.leapdays(1918, 2020)
print(how_many_leap_days)
