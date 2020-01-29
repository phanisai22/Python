import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()
# Month in calendar form
print(calendar.month(2000, 2))
print()
# Month in Matrix form.
print(calendar.monthcalendar(2000, 2))
print()

# Entire Year in Calander view.
print(calendar.calendar(2000))

print(calendar.weekday(2000, 2, 22))
print(calendar.isleap(2000))

how_many_leap_days = calendar.leapdays(2000, 2020)
print(how_many_leap_days)
